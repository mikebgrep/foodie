![Logo](https://github.com/mikebgrep/foodie/blob/master/git_assets/logo.jpeg)

# Foodie
![version](https://img.shields.io/badge/version-1.0.0-green) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

###  Lightweight Rest API with admin panel which manage food recipies easily 
--- 
### Features 
   - 🐍Python Django & Django rest framework based
   - 🛳 Docker image in docker hub for easy deployment ( coming soon )
   - 👨‍🍳 Admin panel revamped with [jazzmin](https://github.com/farridav/django-jazzmin)
   - 🤖 Android application source code for sale on codecanyon ( coming soon )
   - 🔐 Header authentication for easy access managment to the API
   - 🪶 SQLite databse support.
   - 🔎 Pagination support for search endpoint 70 results per page.

### Endpoints 
1. ```GET /category``` - return list of ```category``` object that has ```pk, name``` fields.
2. ```GET /category/pk/recipes```  return list of ```recipe``` object.
3. ```GET /trending``` return list of trendings ```recipes``` objects.
4. ```GET /favorites``` return list of favorites recipies.
   1. ```PATCH /favorites/<int:recipe_pk>/favorite``` - endpoint to favorite and unfavorite recipe.
5. ```GET /tags``` return list of ```tag ``` objects that has ```pk, name``` fields
6. ```GET /tag/pk/recipies``` return list of recipe objects with the current tag.
7. ```POST /api/auth/signup``` endpoint to register admin user.Request body must have  ```username```, ```password``` strings and ```is_superuser``` boolean that should be set to ```True```

📝 Note each recipie object consist of ```['pk', 'name', 'category'*, 'serves', 'tag', 'image', 'video'*, 'ingreadiants', 'instructions']``` (* mean optional)

📝Note the API path is: ```{baseUrl}/api/foodie```

### Admin panel 
![admin](https://github.com/mikebgrep/foodie/blob/master/git_assets/foodie-admin.gif)

📝Note to login in the panel you must register admin user from the ```/signup``` endpoint afterwards the users can be added from the panel.

### Installation 
You can install the server locally as following this guide:
1. Clone the repo and install packages
```
$ git clone https://github.com/mikebgrep/foodie && cd foodie_be
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
```
2. Rename ```.env.examle``` file to ```.env``` open it and enter values for each variable.
    1. For the ```X_AUTH_HEADER``` you can add random GUUID. (this will be the authentication secret *(that will be used for authorization to the API)*
    2. For ```DJANGO_SECRET``` run the following function in terminal and use the output:
```
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
3.Make the migrations and run the server 
```
$ python manage.py makemigrations && python manage.py migrate && python manage.py runserver
```

You can access the admin panel from ```127.0.0.1:8000/admin ``` in browser and ```127.0.0.1:8000/api/foodie``` from Postman or any other client.
Don't forget to add the ```X-Auth-Header``` for each request.

### License
The repository use MIT license
