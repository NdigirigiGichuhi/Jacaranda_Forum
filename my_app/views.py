from my_app import app, db, login
from flask import render_template, flash, redirect, url_for, session
from my_app.forms import LoginForm, SignupForm, PostForm, UpdateProfileForm, EditPostForm
from werkzeug.security import generate_password_hash, check_password_hash
from my_app.models import User, Posts
from flask_login import login_user, login_required, current_user

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    form = SignupForm()

    users = User()

    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        phone = form.phone.data
        email = form.email.data
        password_hash = generate_password_hash(form.password.data)

        if users.query.filter_by(username=username).first():
            flash("use a diffent username")
            return redirect(url_for('sign_up'))
        else:
            user = User(first_name=firstname, last_name=lastname, username=username, phone=phone, email=email, password_hash=password_hash)
            db.session.add(user)
            db.session.commit()

            flash('new user created')
            return redirect(url_for('index'))

    return render_template('sign_up.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        password = form.password.data

        
        if user:
            if check_password_hash(user.password_hash, password):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash('wrong password')
                return redirect(url_for('login'))
        else:
            flash('Wrong username')
            return redirect(url_for('login'))
    
    return render_template('login.html', form=form)
    
@app.route('/dashboard')
@login_required
def dashboard():
    posts = Posts.query.all()

    return render_template('dashboard.html', posts=posts)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/post', methods=[ 'GET', 'POST'])
@login_required
def post():
    form = PostForm()

    if form.validate_on_submit():
        poster = current_user.id
        #author = form.author.data
        content = form.content.data
        post = Posts(poster_id=poster, content=content)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('post.html', form=form)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    form = EditPostForm()
    post = Posts.query.get_or_404(id)

    if form.validate_on_submit():
        post.author = form.author.data
        post.content = form.content.data
        db.session.commit()
        return redirect(url_for('dashboard'))
    
    
    form.author.data = post.author
    form.content.data = post.content    

    return render_template('edit.html', id=id, form=form)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    post = Posts.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/profile')
def profile():
    user = current_user
    return render_template('profile.html', user=user)


@app.route('/update_profile/<int:id>', methods=['GET', 'POST'])
@login_required
def update_profile(id):
    form = UpdateProfileForm()
    user = User.query.get_or_404(id)

    if form.validate_on_submit():
        user.first_name = form.firstname.data
        user.last_name = form.lastname.data
        user.username = form.username.data
        user.email = form.email.data
        user.phone = form.phone.data
        db.session.commit()
        return redirect(url_for('profile'))
    
    form.firstname.data = user.first_name
    form.lastname.data = user.last_name
    form.username.data = user.username
    form.email.data = user.email
    form.phone.data = user.phone

    return render_template('update_profile.html', form=form, id=id, user=user)