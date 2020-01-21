start-clusters:
	kubectl apply -f redis/redis-deploy-ser.yml
	kubectl apply -f services/billing/billing-mongo.yml
	kubectl apply -f services/client/client-mongo.yml
	kubectl apply -f services/fee/fee-mongo.yml
	kubectl apply -f services/order/order-mongo.yml

start-apis:
	kubectl apply -f services/billing/billing-deploy-ser.yml
	kubectl apply -f services/client/client-deploy-ser.yml
	kubectl apply -f services/fee/fee-deploy-ser.yml
	kubectl apply -f services/order/order-deploy-ser.yml


start-gate:
	kubectl create configmap kongconfig --from-file=gateway/conf.d
	kubectl apply -f gateway/gateway-deploy-ser.yaml

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
	kubectl delete -f gateway/gateway-deploy-ser.yaml
	kubectl delete -n default configmap kongconfig


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