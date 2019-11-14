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
		docker stop $(NAME)

pull:
		git pull

rebuild: stop pull build run
