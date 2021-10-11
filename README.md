# Vote for Lunch

## Project Setup in Ubuntu 

```
$ virtualenv -p $(which python3) py3env
$ source py3env/bin/activate
$ git clone https://github.com/shahjalalh/vote_lunch.git
$ cd vote_lunch
$ python manage.py runserver
```

## Requests

### Creating employee or restaurant

### Getting token

```
Request: http://0.0.0.0:8000/api/v1/users/token
Method: POST
Form Fields:
    'username': 'john'
    'password': 'abc'
Response:
    {
        "token": "048122f042c39c5577b2ca456475c39de3125e37"
    }
```