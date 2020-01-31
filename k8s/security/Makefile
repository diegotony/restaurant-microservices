start-clusters:
	sh scripts/create_clusters.sh

start-apis:
	sh scripts/create_apis.sh

start-gate:
	sh scripts/create_kong.sh

start-all:
	sh scripts/create_all.sh

delete-all:
	sh scripts/delete_all.sh

delete-gate:
	sh scripts/delete_kong.sh

check:
	kubectl get pods --watch


testing:
	kubectl apply -f redis/redis-deploy-ser.yml
	kubectl apply -f services/fee/fee-mongo.yml
	kubectl apply -f services/fee/fee-deploy-ser.yml


testing-end:
	kubectl delete -f redis/redis-deploy-ser.yml
	kubectl delete -f services/fee/fee-mongo.yml
	kubectl delete -f services/fee/fee-deploy-ser.yml

.PHONY: start-clusters delete-all start-apis check start-gate start-all