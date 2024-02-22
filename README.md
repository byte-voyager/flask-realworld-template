### Flask project template

> Flask project example.

![](https://raw.githubusercontent.com/Baloneo/flask-realworld-template/main/app/static/flask-logo.png)


### Getting started
Download or clone this project. 

Follow the instructions below:
```shell
pip install poetry
python -m venv .venv
source .venv/bin/activate
poetry install
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
poetry export -f requirements.txt --output requirements.txt
apt install redis
# install docker and docker-compose
make build-image
docker-compose -f docker-compose.yml up -d
```