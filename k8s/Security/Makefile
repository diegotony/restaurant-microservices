 start-clusters:
	sh scripts/create_clusters.sh

start-apis:
	sh scripts/create_apis.sh

start-gate:
	sh scripts/create_kong.sh


delete-all:
	# APIS clusters
	kubectl delete -f redis/redis-deploy-ser.yml
	kubectl delete -f services/billing/billing-mongo.yml
	kubectl delete -f services/client/client-mongo.yml
	kubectl delete -f services/fee/fee-mongo.yml
	kubectl delete -f services/order/order-mongo.yml
	# APIS shutdown
	kubectl delete -f services/billing/billing-deploy-ser.yml
	kubectl delete -f services/client/client-deploy-ser.yml
	kubectl delete -f services/fee/fee-deploy-ser.yml
	kubectl delete -f services/order/order-deploy-ser.yml
	# Gateway shutdown
	#kubectl delete -f gateway/gateway-deploy-ser.yaml
	#kubectl delete -n default configmap kongconfig
	kubectl delete -f kong/kong.yml


delete-gate:

	# kubectl delete -f gateway/gateway-deploy-ser.yaml
	# kubectl delete -n default configmap kongconfig
	kubectl delete -f kong/paths.yml
	kubectl delete -f kong/plugins.yml



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

.PHONY: start-clusters delete-all start-apis check start-gate