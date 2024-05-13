from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, EmailField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, equal_to
from wtforms.widgets import TextArea




#login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'Username', 'size': '50'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password', 'size': '50'})
    submit = SubmitField('Login')


#sign up form
class SignupForm(FlaskForm):
    firstname = StringField('Fist Name', validators=[DataRequired()], render_kw={'placeholder': 'First Name', 'size': '50'})
    lastname = StringField('Last Name', validators=[DataRequired()], render_kw={'placeholder': 'Last Name', 'size': '50'})
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'Username', 'size': '50'})
    phone = StringField('Phone number', validators=[DataRequired()], render_kw={'placeholder': 'Phone', 'size': '50'})
    email = EmailField('Email', validators=[DataRequired()], render_kw={'placeholder': 'Email', 'size': '50'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password', 'size': '50'})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={'placeholder': 'Confirm Password', 'size': '50'})
    submit = SubmitField('Register')

#posts form
class PostForm(FlaskForm):
    #author = StringField('Author', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()], widget=TextArea(), render_kw={'size': '1000'})
    submit = SubmitField('Post')


# edit post form
class EditPostForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()], widget=TextArea(), render_kw={'size': '1000'})
    submit = SubmitField('Post')


#update user profile
class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('Fist Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    phone = StringField('Phone number', validators=[DataRequired()])
    submit = SubmitField('Update')