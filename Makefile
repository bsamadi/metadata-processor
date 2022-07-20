build-prod:
	docker build -t bsamadi/metadata-processor:latest -f ./binder/Dockerfile.prod .

push-prod:
	docker push bsamadi/metadata-processor:latest

run-prod:
	docker 