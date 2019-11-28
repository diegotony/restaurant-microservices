FILE :=  docker-compose.yaml
IMAGE := diegotony/kong-nodb:1.0


build:
	docker build  -t $(IMAGE) . --no-cache

up-server:
	docker build  -t $(IMAGE)b . --no-cache
	docker-compose -f $(FILE) up -d
	./ngrok http http://localhost:8000



down-server:
	docker-compose -f $(FILE) down


upgrade-image:
	docker push $(IMAGE)

.PHONY: up-server down-server upgrade-image