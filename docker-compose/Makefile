

GIT_TAG := $(shell git describe --abbrev=0 --tags)
CI_COMMIT_SHORT_SHA := $(shell git rev-parse --short=8 HEAD)

api-latest:
	docker build -f api/api.Dockerfile -t test_api:latest .

api:
	docker-compose -f api/docker-compose.api.yml build


