NAME = dga_intel

default:
		flask run --host=0.0.0.0 --port=80

run:
		docker-compose up -d

install:
		pip install -r requirements.txt

build:
		docker build -t $(NAME) .
		docker network create dga_intel

stop:
		docker-compose stop

pull:
		git pull

deploy:
		(git pull | egrep 'up to date') || make rebuild
		
test:
		python test.py

rebuild: pull stop build run

up:
	docker-compose up
