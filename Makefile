DOCKER_USER?=bsamadi

build-prod:
	docker build -t $(DOCKER_USER)/metadata-processor:latest -f ./binder/Dockerfile.prod .

push-prod:
	docker push $(DOCKER_USER)/metadata-processor:latest

run-mp:
	docker-compose up -d

stop-mp:
	docker-compose down

flask:
	flask run