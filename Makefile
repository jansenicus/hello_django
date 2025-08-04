# Makefile for Django + Docker (Dev, Staging, Prod)

# Compose aliases
DEV_COMPOSE=docker-compose -f docker-compose.yml
STAGING_COMPOSE=docker-compose -f docker-compose.staging.yml
PROD_COMPOSE=docker-compose -f docker-compose.prod.yml

# Exec aliases
DEV_EXEC=$(DEV_COMPOSE) exec web
STAGING_EXEC=$(STAGING_COMPOSE) exec web
PROD_EXEC=$(PROD_COMPOSE) exec web

# Docker image settings
APP_NAME := hello_django
DOCKER_REGISTRY := docker.io/jansenicus
GIT_SHA := $(shell git rev-parse --short HEAD)
DATE := $(shell date +%Y%m%d)

.PHONY: dev-up dev-down dev-restart dev-build dev-migrate dev-collectstatic dev-logs dev-image dev-push \
        staging-up staging-down staging-restart staging-build staging-migrate staging-collectstatic staging-logs staging-image staging-push \
        prod-up prod-down prod-restart prod-build prod-migrate prod-collectstatic prod-logs prod-image prod-push

## Development
dev-up:
	@$(DEV_COMPOSE) up -d

dev-down:
	@$(DEV_COMPOSE) down -v

dev-restart: dev-down dev-build dev-up

dev-build:
	@$(DEV_COMPOSE) build

dev-migrate:
	@$(DEV_EXEC) python manage.py migrate --noinput

dev-collectstatic:
	@$(DEV_EXEC) python manage.py collectstatic --no-input --clear

dev-logs:
	@$(DEV_COMPOSE) logs -f

dev-image:
	docker build -f Dockerfile.dev -t $(DOCKER_REGISTRY)/$(APP_NAME):dev-$(GIT_SHA) .

dev-push:
	docker push $(DOCKER_REGISTRY)/$(APP_NAME):dev-$(GIT_SHA)

## Staging
staging-up:
	@$(STAGING_COMPOSE) up -d

staging-down:
	@$(STAGING_COMPOSE) down -v

staging-restart: staging-down staging-build staging-up

staging-build:
	@$(STAGING_COMPOSE) build

staging-migrate:
	@$(STAGING_EXEC) python manage.py migrate --noinput

staging-collectstatic:
	@$(STAGING_EXEC) python manage.py collectstatic --no-input --clear

staging-logs:
	@$(STAGING_COMPOSE) logs -f

staging-image:
	docker build -f Dockerfile.staging -t $(DOCKER_REGISTRY)/$(APP_NAME):staging-$(DATE) .

staging-push:
	docker push $(DOCKER_REGISTRY)/$(APP_NAME):staging-$(DATE)

## Production
prod-up:
	@$(PROD_COMPOSE) up -d

prod-down:
	@$(PROD_COMPOSE) down -v

prod-restart: prod-down prod-build prod-up

prod-build:
	@$(PROD_COMPOSE) build

prod-migrate:
	@$(PROD_EXEC) python manage.py migrate --noinput

prod-collectstatic:
	@$(PROD_EXEC) python manage.py collectstatic --no-input --clear

prod-logs:
	@$(PROD_COMPOSE) logs -f

prod-image:
	docker build -f Dockerfile -t $(DOCKER_REGISTRY)/$(APP_NAME):latest .

prod-push:
	docker push $(DOCKER_REGISTRY)/$(APP_NAME):latest