DOCKER_IMAGE_NAME = philingood/crazy-bot
DOCKERFILE_PATH = ./Dockerfile
CONTAINER_NAME = crazy-bot
ENV_FILE = .env

.PHONY: docker_build docker_run docker
docker_build:
	docker build -t $(DOCKER_IMAGE_NAME) -f $(DOCKERFILE_PATH) .

docker_run: docker_stop
	docker run \
		--name $(CONTAINER_NAME) \
		--env-file .env \
		--restart=unless-stopped \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-d \
		$(DOCKER_IMAGE_NAME)

docker_stop:
	docker stop $(CONTAINER_NAME) && docker rm $(CONTAINER_NAME)

docker: docker_build docker_run

.PHONY: build cmd local
build:
	pyinstaller --onefile src/bot.py

cmd:
	./dist/bot

local: build cmd

.PHONY: run
run:
	python src/bot.py

.PHONY: test
test:
	PYTHONPATH=src pytest -m required -v

.PHONY: test_mode
test_mode: docker_stop docker_build
	docker run \
		--name $(CONTAINER_NAME) \
		--env-file $(ENV_FILE) \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-d \
		$(DOCKER_IMAGE_NAME)
