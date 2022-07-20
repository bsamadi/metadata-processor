DOCKER_USER?=bsamadi

docker-build:
	docker build -t $(DOCKER_USER)/metadata-processor:latest -f ./binder/Dockerfile.prod .

# docker-push and docker-pull
docker-%:
	docker $* $(DOCKER_USER)/metadata-processor:latest

start:
	docker-compose up -d

stop:
	docker-compose down

requirements:
	pip3 install -r requirements.txt

flask:
	flask run

gunicorn:
	gunicorn -w 3 -b "0.0.0.0:5000" -t 30 --reload wsgi:app

flake8:
	flake8 --exclude env --ignore E402,E501 .

black:
	black --exclude=env .

api_test:
	@./tests/api_test.sh

pytest:
	python3 -m pytest

unittest:
	python3 -m unittest discover -s tests -p '*_unittest.py'