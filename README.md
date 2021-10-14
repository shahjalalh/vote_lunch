# Vote for Lunch

Python: 3.8.x (recommended)

In Dockerfile ```3.8.12-slim-buster``` is used for deployment.

> ```PyLint```, ```iSort``` is used as well as **PEP8** rules are followed.

## Project Setup in Ubuntu 

```
$ virtualenv -p $(which python3) py3env
$ source py3env/bin/activate
$ git clone https://github.com/shahjalalh/vote_lunch.git
$ cd vote_lunch
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8000
```

## Project Setup in Docker
Need docker and docker compose installed in the system.
```
$ docker-compose up --build
``` 

Stop the docker-compose
```
$ docker-compose down
```

## Requests

```CornerCaseLunchAPI.postman_collection.json``` file contains postman collection of api with example.

### Creating employee or restaurant
```
A single API to create a employee or a restaurant. Both employee and restaurant can not contain same data.

Args:
    request ([POST]): http://0.0.0.0:8000/api/v1/users/register
    Form Fields:
        'username': 'john'
        'first_name': 'John'
        'last_name': 'Doe'
        'email': 'john.doe@gmail.com'
        'password': 'super-secret-pass'
        'employee': True
        'restaurant': False

Returns:
    {
        "id": 5,
        "username": "john"
    }
    or,
    {
        "error": "Invalid data"
    }
```

### Getting token

```
Request: http://0.0.0.0:8000/api/v1/users/login
Method: POST
Form Fields:
    'username': 'john'
    'password': 'abc'
Response:
    {
        "token": "048122f042c39c5577b2ca456475c39de3125e37"
    }
```

### Logout
```
Logout the user

Args:
    request ([POST]): http://0.0.0.0:8000/api/v1/users/logout
    Form Fields:
        'token': '0066f17d9199a0ae62db97a8b3051efc612128a7'

Returns:
    Status: 205 Reset Content
```

### Submitting New Menu
```
Create menu API for the restaurent. Only restaurant can create menu not employee.

Args:
    request ([POST]): http://0.0.0.0:8000/api/v1/menu/create
    Authorization: Token 342b58233e5fdeb2446bcaae60b6e51e953f7a17
    Form Fields:
        'name': 'Nasi goreng, Pasta, Rice'
        'detail': 'Lorem Ipsum is simply dummy text of the printing
        and typesetting industry. Lorem Ipsum has been the
        industry's standard dummy text ever since the 1500s, when
        an unknown printer took a galley of type and scrambled it
        to make a type specimen book.'
        'price': 3.30

Returns:
    {
        "id": 5,
        "name": "Nasi goreng, Pasta, Rice",
        "created_date": "2021-10-13"
    }
```

### Today Menu List

```
This view should return a list of all the menu for current date. This API does not require Authorization token. Have done it intensionally.

Args:
    request ([GET]): http://0.0.0.0:8000/api/v1/menu/today

Returns:
    [
        {
            "id": 6,
            "name": "Nasi goreng, Pasta, Steak",
            "restaurant": "Handi Mama",
            "detail": "Lorem Ipsum is simply dummy text of the
            printing and typesetting industry. Lorem Ipsum has
            been the industry's standard dummy text ever since
            the 1500s, when an unknown printer took a galley of
            type and scrambled it to make a type specimen book.",
            "price": "13.30",
            "created_date": "2021-10-14"
        }
    ]
```

### Vote for particular menu

```
Vote for a menu. Only employee can vote for a menu not restaurant.

Args:
    request ([POST]): http://0.0.0.0:8000/api/v1/menu/vote

    Authorization: Token 342b58233e5fdeb2446bcaae60b6e51e953f7a17

    Form Fields:
        'id': 5

Returns:
    {
        "id": 5,
        "name": "Nasi goreng2",
        "created_date": "2021-10-13",
        "votes": 1
    }
```

### Get winner restaurant
```
Vote for a menu. Only employee can vote for a menu not restaurant.

Args:
    request ([GET]): http://0.0.0.0:8000/api/v1/menu/winner

    Authorization: Token 342b58233e5fdeb2446bcaae60b6e51e953f7a17

Returns:
    {
        "id": 11,
        "name": "The Cafe Rio"
    }
```

> For time limitation, only few test cases is written.
