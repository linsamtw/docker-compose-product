

GIT_TAG := $(shell git describe --abbrev=0 --tags)
CI_COMMIT_SHORT_SHA := $(shell git rev-parse --short=8 HEAD)

api-latest:
	docker build -f api.Dockerfile -t test:latest .

api:
	docker build -f api.cache.Dockerfile -t test:dev .



