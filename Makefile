DOCKER_USER?=bsamadi

docker-build:
	docker build -t $(DOCKER_USER)/metadata-processor:latest -f ./binder/Dockerfile.prod .

# docker-push and docker-pull
docker-%:
	docker $* $(DOCKER_USER)/metadata-processor:latest

run-mp:
	docker-compose up -d

stop-mp:
	docker-compose down

requirements:
	pip3 install -r requirements.txt

flask:
	flask run

gunicorn:
	gunicorn -w 3 -b "0.0.0.0:5000" -t 30 --reload wsgi:app