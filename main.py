# ======================================================================
# main.py: app driver 
# ==> Fetches data from database and sends the response to client side
# ==> The API can be tested using Postman 
# ==> To start the server and enable the endpoints 
# # Run "python3 main.py"
# ======================================================================


from app import app, db, ma, jwt, mail
from models import User, Recipe, UserSchema, RecipeSchema
from flask import jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token


### routes 
@app.route('/')
def home(): 
    return 'Welcome to Sophie food blog'

@app.route('/not_found')
def not_found(): 
    return jsonify(message='that resource was not found!'),404


# user login
@app.route('/login', methods=['POST'])
def login(): 
    # check if the object is json format
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else: 
        email = request.form['email']
        password = request.form['password']

    test = User.query.filter_by(email=email, password=password).first()
    if test: 
        access_token = create_access_token(identity=email)
        return jsonify(message='Login succeeded!', access_token=access_token)
    else: 
        return jsonify(message='Bad email or password'), 401



# user registration
@app.route('/register', methods=['POST'])
def register(): 
    email = request.form['email']
    test = User.query.filter_by(email=email).first()
    if test: 
        return jsonify(message='That email already exists'),409
    else: 
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify(message='User created successfully'), 201

# retrieve the password
@app.route('/retrieve_password/<string:email>', methods=['GET'])
def retrieve_password(email:str):
    user = User.query.filter_by(email=email).first()
    if user: 
        msg = Message("Your FoodRecipe API password is "+ user.password, 
                sender="admin@foodrecipe-api.com",
                recipients=[email])
        mail.send(msg)
        return jsonify(message="Password sent to "+ email)
    else:
        return jsonify(message="That email doesn't exist"),401




# get all the recipes 
@app.route('/recipes', methods=['GET'])
def recipes(): 
    # get all the list of recipes 
    recipe_list = Recipe.query.all()
    result = recipes_schema.dump(recipe_list)
    return jsonify(result)

# get a specific recipe
@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def recipe(recipe_id:int):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    if recipe: 
        result = recipe_schema.dump(recipe)
        return jsonify(result)
    else: 
        return jsonify(message="The recipe is not found!"),404



# add a new recipe 
@app.route('/add_recipe', methods=['POST'])
@jwt_required()
def add_recipe(): 
    recipe_name = request.form['recipe_name']
    print(recipe_name)
    recipe = Recipe.query.filter_by(recipe_name=recipe_name).first()
    print('recipe is ', recipe)
    # 409 : conflict 
    if recipe: 
        return jsonify("There is already a recipe by that name"),409
    else: 
        # print("This recipe name is good to add ")
        recipe_type = request.form['recipe_type']
        print(recipe_type)
        recipe_cuisine = request.form['recipe_cuisine']
        print(recipe_cuisine)
        recipe_ingredient = request.form['recipe_ingredient']
        recipe_prep_time = request.form['recipe_prep_time']
        print(recipe_type, recipe_cuisine, recipe_ingredient, recipe_prep_time)
        new_recipe = Recipe(recipe_name=recipe_name, 
                            recipe_cuisine=recipe_cuisine,
                            recipe_ingredient=recipe_ingredient,
                            recipe_type=recipe_type,
                            recipe_prep_time=recipe_prep_time)
        print("new recipe", new_recipe)

        db.session.add(new_recipe)
        db.session.commit()

        return jsonify(message="You successfully added a recipe"),201

# update a recipe 
@app.route('/update_recipe', methods=['PUT'])
@jwt_required()
def update_recipe():
    recipe_id = int(request.form['recipe_id'])
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    print(recipe_id, recipe)
    if recipe:
        print("updating recipe")
        recipe.recipe_name = request.form['recipe_name']
        recipe.recipe_type = request.form['recipe_type']
        recipe.recipe_cuisine = request.form['recipe_cuisine']
        recipe.recipe_ingredient = request.form['recipe_ingredient']
        recipe.recipe_prep_time = request.form['recipe_prep_time']
        db.session.commit()
        return jsonify(message="You updated a recipe"), 202
    else:
        return jsonify(message="That recipe does not exist"), 404


@app.route('/delete_recipe/<int:recipe_id>', methods=['DELETE'])
@jwt_required()
def delete_recipe(recipe_id: int):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        return jsonify(message="You deleted a recipe"), 202
    else:
        return jsonify(message="That recipe does not exist"), 404



# create schema to deserialization
user_schema = UserSchema()
users_schema = UserSchema(many=True)

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)





if __name__== '__main__':
    app.run()

