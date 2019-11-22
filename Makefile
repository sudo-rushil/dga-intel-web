NAME = dga_intel

default:
		flask run --host=0.0.0.0 --port=80

run:
		docker run --name $(NAME) -d --rm -p 80:80 $(NAME)

install:
		pip install -r requirements.txt

build:
		docker build -t $(NAME) .

stop:
		docker stop $(NAME) || echo stopped

pull:
		git pull

deploy:
		(git pull | egrep 'up to date') || make rebuild
		
test:
		python test.py

rebuild: pull stop build run

