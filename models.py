# ===========================================================
# models.py
# ==> Define the database schemas: User and Recipe schemas  
# ==> Uses SQLite database
# ===========================================================


from app import db,ma, jwt, mail
from sqlalchemy import Column, Integer, String, Float

# create the ORM database model class
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name= Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    region = Column(String)
    
class Recipe(db.Model):
    __tablename__ = 'recipes'
    recipe_id = Column(Integer, primary_key=True)
    recipe_name = Column(String)
    recipe_cuisine = Column(String)
    recipe_ingredient = Column(String)
    recipe_type = Column(String)
    recipe_prep_time = Column(String)


# serialization 
class UserSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'first_name', 'last_name', 'email','password','region')

class RecipeSchema(ma.Schema):
    class Meta: 
        fields = ('recipe_id','recipe_name', 'recipe_cuisine','recipe_ingredient','recipe_prep_time')




