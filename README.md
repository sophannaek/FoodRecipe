# FoodRecipe
A REST API for a food recipe site. 

# Endpoints

## Get Recipes
* URL 
/recipes

* Method: 
`GET
`
* URL Params:
None

* Data Params: 
None

* Success Response: 
** Code: 200

* Error Response: 
** Code: 401

* Sample Call:
```bash
 $.ajax({
    url: "/recipes",
    dataType: "json",
    type : "GET",
    success : function(r) {
      console.log(r);
    }
  });

```


## Get a specific recipe
* URL 
/recipe/:id

* Method: 
`GET
`
* URL Params:
` id=[integer]`

* Data Params: 
None

* Success Response: 
** Code: 200
    Content: `{id: 1,recipe_name='Pad Thai', recipe_cuisine='Thai',recipe_ingredient='rice noodle, eggs, chicken, madarin sauce, peanut', recipe_type='Main dish', recipe_prep_time='1 hr'}`

* Error Response: 
** Code: 401
    Content: `{message:The recipe is not found!}`

## Add a new recipe
* URL 
/add_recipe

* Method: 
`POST
`
* URL Params:
`None`


* Data Params: 
```bash
 recipe_name = [String]
 recipe_cuisine =[String]
 recipe_type = [String]
 recipe_ingredient=[String]
 recipe_type = [String]
 recipe_prep_time =[String]
```

* Success Response: 
** Code: 200
    Content: `{message: You successfully added a recipe}`

* Error Response: 
** Code: 401
    Content: `{message: There is already a recipe by that name!}`


## Update an existing recipe
* URL 
/update_recipe

* Method: 
`PUT`
* URL Params:
`None`


* Data Params: 
```bash
 recipe_id = [Integer]
 recipe_name = [String]
 recipe_cuisine =[String]
 recipe_type = [String]
 recipe_ingredient=[String]
 recipe_type = [String]
 recipe_prep_time =[String]
 ```

* Success Response: 
** Code: 200
    Content: `{message: You successfully updated a recipe}`

* Error Response: 
** Code: 402
    Content: `{message: That recipe does not exist!}`


## Delete a recipe
* URL 
/delete_recipe/:id

* Method: 
`DELETE`
* URL Params:
`id=[Integer]`


* Data Params: 
`None`

* Success Response: 
** Code: 202
    Content: `{message: You successfully deleted a recipe}`

* Error Response: 
** Code: 404
    Content: `{message: That recipe does not exist!}`


## Update an existing recipe
* URL 
/update_recipe

* Method: 
`PUT`
* URL Params:
`None`


* Data Params: 
```bash
 recipe_id = [Integer]
 recipe_name = [String]
 recipe_cuisine =[String]
 recipe_type = [String]
 recipe_ingredient=[String]
 recipe_type = [String]
 recipe_prep_time =[String]
 ```

* Success Response: 
** Code: 200
    Content: `{message: You successfully updated a recipe}`

* Error Response: 
** Code: 401
    Content: `{message: That recipe does not exist!}`

## User Registration
* URL 
/register

* Method: 
`POST`

* URL Params:
`None`

* Data Params: 
```bash
email = [String]
first_name= [String]
last_name = [String]
password = [String]
region= [String]
```

* Success Response: 
** Code: 201
    Content: `{message: User created successfully}`

* Error Response: 
** Code: 401
    Content: `{message: That email already exists!}`


## User Login
* URL 
/login

* Method: 
`POST`

* URL Params:
`None`

* Data Params: 
```bash
email = [String]
password = [String]
```

* Success Response: 
** Code: 201
    Content: `{message: Login succeeded!}`

* Error Response: 
** Code: 401
    Content: `{message: Bad email or password}`

## Password Retrieval 
* URL 
/retrieve_password/:email

* Method: 
`POST`

* URL Params:
`None`

* Data Params: 
```bash
email = [String]
last_name = [String]
password = [String]
```

* Success Response: 
** Code: 201
    Content: `{message: Password sent to 'email'}`

* Error Response: 
** Code: 401
    Content: `{message: That email doesn't exist!}`



# Common Setup
Clone the repo and install the independencies 

```bash
git clone https://github.com/sophannaek/FoodRecipe.git

```

use the package manager [pip](https://packaging.python.org/tutorials/installing-packages/)

```bash
pip install -r requirements.txt 

or 

pip3 install -r requirements.txt
```

# Test/Access the API
All endpoints can be tested using a free tool: [Postman](https://www.postman.com)