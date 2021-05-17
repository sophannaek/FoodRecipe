# ====================================================================
# app.py 
# ==> initialize the app and the starts the server for the application
# ==> REST API: endpoints for food recipes 
# =====================================================================

'''
Application name: lunch picker or recipe recommendation 
Backend: endpoints for lunch picker application 
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Mail, Message 

# define the applciation 
app = Flask(__name__)
# database file directory 
basedir = os.path.abspath(os.path.dirname(__file__))

# configure SQLAlchemy database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'recipes.db')
# JWT token configuration 
app.config['JWT_SECRET_KEY'] = 'secret phrase'  # change this to your own password 
# email configuration 
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# define the database 
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
mail = Mail(app)




# ------------------------------------------ #
from models import Recipe, User

# creating the database with with the Flask CLI 
@app.cli.command('db_create')
def db_create(): 
    db.create_all()
    print("Database created!")

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped')


# seeding data into the database 
@app.cli.command('db_seed')
def db_seed(): 
    custard = Recipe(recipe_name='Egg Custard',
                    recipe_cuisine='none',
                    recipe_ingredient='milk, eggs, sugar, salt, vanilla',
                    recipe_type='Dessert',
                    recipe_prep_time='1 hr')
    padThai = Recipe(recipe_name='Pad Thai',
                    recipe_cuisine='Thai',
                    recipe_ingredient='rice noodle, eggs, chicken, madarin sauce, peanut',
                    recipe_type='Main dish',
                    recipe_prep_time='1 hr')

    chickenSalad = Recipe(recipe_name='Chicken Salad',
                    recipe_cuisine='Western',
                    recipe_ingredient='chicken, boiled eggs, lettuce, dressing, pease, cheese',
                    recipe_type='Main dish',
                    recipe_prep_time='20 mins')
    
    brocolliSoup = Recipe(recipe_name='Brocolli Soup',
                    recipe_cuisine='Western',
                    recipe_ingredient='brocolli, chicken broth, milk, all-purpose flour',
                    recipe_type='Soup',
                    recipe_prep_time='35 mins')

    db.session.add(custard)
    db.session.add(padThai)
    db.session.add(chickenSalad)
    db.session.add(brocolliSoup)

    admin = User(first_name='admin',last_name='user',email='admin@user.com', password='password')

    db.session.add(admin)
    db.session.commit()
    print("Database seeded!")




