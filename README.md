[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bsamadi/metadata-processor/main)

# metadata-processor
This repository contains a Flask implementation of a REST API to process image metadata.  

## Development

- Clone the repository.
- Open the folder with VS Code.
- Click on the bottom left corner and choose "Open Folder in Container".
- Press Ctrl+` to open a terminal.
- You have two options to test the API
  - Running a server:
    - Run `make flask` to the Flask development server or `make gunicorn` to run the gunicorn server.
    - Open another terminal and run: `make api_test` or `./tests/api_test.sh` to send a JSON object to the API server.
  - Running Python tests:
    - Run `make pytest` to run pytest tests

# Make commands

- Build the Docker image: `make DOCKER_USER=bsamadi docker-build`
- Push the Docker image to hub.docker.com: `make DOCKER_USER=bsamadi docker-push`
- Pull the Docker image from hub.docker.com: `make DOCKER_USER=bsamadi docker-pull`
- Run the API in a Docker container: `make start`
- Stop the Docker container: `make stop`
- Install the Python requirements: `make requirements`
- Run the Flask development server: `make flask`
- Run the Gunicorn server: `make gunicorn`
- Lint the code with Flake8: `make flake8`
- Autoformat files with Black: `make black`
- Run unittest tests: `make unittest`
- Run pytest tests: `make pytest`

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
  - [x] Pytest
  - [x] Unittest
- [x] Linting
  - [x] Flake8
  - [x] Black
- [ ] Folder structure
- [ ] Deploy to Heroku
- [ ] Deploy to a (cloud or local) Kubernetes cluster with HTTPS
- [ ] Deploy to a (cloud or local) Nomad cluster with HTTPS