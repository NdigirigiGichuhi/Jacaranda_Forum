from flask_sqlalchemy import SQLAlchemy
from my_app import db, Migrate, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name =db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), index=True, nullable=False)
    phone = db.Column(db.Integer, index=True, nullable=False)
    email = db.Column(db.String, index=True, nullable=False)
    password_hash = db.Column(db.String(50), nullable=False)
    #user can have many posts
    posts = db.relationship('Posts', backref='poster')


    @property
    def password(self):
        return 'not readable'
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    
    def clear_table(self, table):
        table.query.delete()
        db.session.commit()


#posts class
class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    #author = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    #create a foreign key (refer to the primary key of the user)
    poster_id = db.Column(db.Integer, db.ForeignKey('users.id'))
