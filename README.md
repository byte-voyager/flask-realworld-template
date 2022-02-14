### Flask realworld template

Flask project example.

* CURD
* HTML template
* JWT Auth
* Marshmallow JSON validator
* Peewee ORM
* Redis
* Blueprint
* Docker deploy
* Code formatting

### Getting started
Download or clone this project. 

Suggest Python3.6+, develop on a Linux distribution.

Follow the instructions below(using pipenv):
```shell
pip install pipenv
cd path/of/this/project
mkdir .venv
pipenv install
piennv shell
```
or using `virtualenv`
```shell
cd path/of/this/project
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

init database
```shell
cd path/of/this/project
cd deploy/
apt install docker.io  # You may need to configure the mirror
apt install docker-compose # or pip install docker-compose
docker-compose -f mysql-docker-compose.yml up -d
cd ..
python manage.py -c # create tables
apt install redis
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

init tables
```shell
python manager.py -c
```

lint code
```shell
pipenv intall -d  # install dev packages
make lint
```

deploy
```shell
apt install redis
# install docker and docker-compose
make build-image
docker-compose -f docker-compose.yml up -d
```