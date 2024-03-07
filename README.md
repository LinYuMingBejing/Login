## Folder Structrue
```
├── app
│   ├── api
│   │   ├── ....    => API related development
│   ├── settings
│   ├── models.py    => Model config
│   ├── schema.py    => Input schema
├── docker           => Build image scripts
├── migrations       => DB Migrate
├── .gitignore
├── Dockerfile
├── .......
└── uwsgi.ini
```

### Run SENAO application 
```
$ cd docker
$ sudo docker-compose up --build -d
```

### DB Migration
```
$ python3 manage.py db init
$ python3 manage.py db migrate
$ python3 manage.py db upgrade
```

## Unit Test
### Create account
* Request 
```
curl -X POST \
    http://localhost/user \
    -d '{"username": "senao", "password": "aA20240305"}'
```
* Response

|  Status Code  | Message    |
| --------    | -----| 
| 201         | {"payload": null,"reason": "Account was created successfully.", "success": true}| 
| 409        | {"payload": null, "reason": "Username is existed.", "success": false}|
| 422        | {"payload": null, "reason": {"password": ["Password must be a string between 8 and 32 letters.", "Password must contain at least 1 uppercase letter, 1 lowercase letter, and 1 number."], "username": ["Username must be a string between 3 and 32 letters."]}, "success":false}  | 


### Login
* Request 
```
curl -X POST \
    http://localhost/login \
    -d '{"username": "senao", "password": "aA20240305"}'
```
* Response

|  Status Code  | Message    |
| --------    | -----| 
| 200        |{"payload": {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJhcHAzIiwiZXhwIjoxNzA5NzcyOTA2fQ.jwxhqvLpirBFb4BZgESnvMDxj1rolPrdcNyNG3AEr68"}, "reason": "Login success.", "success": true} | 
| 404        | {"payload": null, "reason": "User not found.", "success": false}  | 
| 404        | {"payload": null, "reason": "Password not correct.", "success": false} |  


### Request with JWT Token
* Request 
```
curl http://localhost/about/me \
  -H "Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJhcHAzIiwiZXhwIjoxNzA5NzczMTMzfQ.AEj9lbm8CJk8yd9VluoBFkCs15JHT8sBmOZetX6Ilz4" 
```
* Response

|  Status Code  | Message    |
| --------    | -----| 
| 200        |{"code": 200, "message": "The action perform successfully."}| 
| 401        | {"payload": null, "reason": "Unauthorized.","success": false} | 
| 403        | {"payload": null, "reason": "Forbidden.","success": false} |  