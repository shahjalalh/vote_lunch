# Vote for Lunch

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