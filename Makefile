DOCKER_COMPOSE_CMD=$(shell echo 'docker-compose')
USERNAME=$(shell whoami)

up:
	$(DOCKER_COMPOSE_CMD) up -d
down:
	$(DOCKER_COMPOSE_CMD) down
restart: down up

pylint:
	find . -name "*.py" -exec pylint --rcfile=.pylintrc '{}' +
pycodestyle:
	pycodestyle --max-line-length=119 .
