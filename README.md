# User Management in Django Rest Framework


## Steps
- Create a venv and activate it:
```
python3 -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```
- Run pip from requeriments.txt: ```pip install -r /path/to/requirements.txt```
- Run make migrations: ``` python manage.py makemigrations```
- Run make migrate: ``` python manage.py migrate```
- Run runserver: ``` python manage.py runserver```

### I'm sending an export of requestes from postman, file:
```Danilo.postman_collection.json```
just import to your postman and follow the numbers

1 - Signup
2 - Signin
3 - Me

## Heroku
- This project is on Heroku: https://user-management-danilo.herokuapp.com/

## Endpoints
- POST https://user-management-danilo.herokuapp.com/api/signup/

```
{
    "first_name": "Jon",
    "last_name": "Doe",
    "email": "jon@doe.com",
    "password":"123456",
    "phones":[
        {
            "number": 999998888,
            "area_code": 11,
             "country_code": "+55"
        }
    ]
}
```

- POST https://user-management-danilo.herokuapp.com/api/signin/
```
{
    "email":"jon@doe.com",
    "password":"123456"
}
```
- GET https://user-management-danilo.herokuapp.com/api/me/