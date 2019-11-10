default:
	flask run --host=0.0.0.0 --port=80

run:
	docker run -d --rm -p 80:80 ai_dga

install:
	pip install -r requirements.txt

build:
	docker build -t ai_dga .
