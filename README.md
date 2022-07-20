[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bsamadi/metadata-processor/main)

# metadata-processor
This repository contains a Flask implementation of a REST API to process image metadata.  

# Make commands

- Build the Docker image: `make DOCKER_USER=bsamadi docker-build`
- Push the Docker image to hub.docker.com: `make DOCKER_USER=bsamadi docker-push`
- Pull the Docker image to hub.docker.com: `make DOCKER_USER=bsamadi docker-pull`
- Run the API in a Docker container: `make start`
- Stop the Docker container: `make stop`
- Install the Python requirements: `make requirements`
- Run the Flask development server: `make flask`
- Run the Gunicorn server: `make gunicorn`
- Lint the code with Flake8: `make flake8`
- Autoformat files with Black: `make black`

# References

* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Pysolar](https://pysolar.org/)

# Features

- [x] VS Code Devcontainer
- [x] Makefile
- [x] [Binder](https://mybinder.org/) compatible
  - [x] `requirements.txt`
  - [x] `apt.txt`
- [x] Production Docker image
  - [x] `docker-compose`
- [x] Tests
  - [x] API
  - [x] Python
- [x] Linting
  - [x] Flake8
  - [x] Black