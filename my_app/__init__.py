from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager 



app = Flask(__name__)
app.config['SECRET_KEY'] = "don't try"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'



from my_app import views