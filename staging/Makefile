FILE :=  docker-compose.yaml
IMAGE := diegotony/kong-nodb:1.0


build:
	docker build  -t $(IMAGE) . --no-cache

up-server:
	docker build  -t $(IMAGE)b . --no-cache
	docker-compose -f $(FILE) up -d
	./ngrok http http://localhost:8000

update-images:
	docker pull diegotony/orden-micro:k8s
	docker pull diegotony/fee-micro:k8s
	docker pull diegotony/client-micro:k8s


down-server:
	docker-compose -f $(FILE) down


upgrade-image:
	docker push $(IMAGE)

.PHONY: up-server down-server upgrade-image