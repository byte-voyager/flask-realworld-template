### Flask realworld template

> Flask project example.

![](https://raw.githubusercontent.com/Baloneo/flask-realworld-template/main/app/static/flask-logo.png)

* CURD
* HTML template
* JWT Auth
* Marshmallow JSON validator
* Peewee ORM
* PostgreSQL
* Redis
* rye
* Docker deploy
* Code formatting

### Getting started
Download or clone this project. 

Follow the instructions below(using pipenv):
```shell
rye sync
source .venv/bin/activate
```

init database
```shell
cd path/of/this/project
cd deploy/
apt install docker.io
apt install docker-compose # or pip install docker-compose
apt install redis
docker-compose -f pg-docker-compose.yml up -d
cd path/of/this/project
python manage.py -c # create tables
```

run server
```shell
python manage.py
```

### Other...
specify port
```shell
python manager.py -p 8888  
```

lint code
```shell
make lint
```

deploy
```shell
apt install redis
# install docker and docker-compose
make build-image
docker-compose -f docker-compose.yml up -d
```