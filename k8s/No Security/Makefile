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
	kubectl apply -f kong/paths.yml
	kubectl apply -f kong/plugins.yml

	kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "rl-by-ip\n"}}}'
	kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-id\n"}}}'
	kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "cors\n"}}}'
	kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-termination\n"}}}'
	kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "bot-detection\n"}}}'

	kubectl patch svc client-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "rl-by-ip\n"}}}'
	kubectl patch svc client-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-id\n"}}}'
	kubectl patch svc client-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "cors\n"}}}'
	kubectl patch svc client-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-termination\n"}}}'
	kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "bot-detection\n"}}}'

	kubectl patch svc fee-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "rl-by-ip\n"}}}'
	kubectl patch svc fee-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-id\n"}}}'
	kubectl patch svc fee-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "cors\n"}}}'
	kubectl patch svc fee-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-termination\n"}}}'
	kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "bot-detection\n"}}}'
	

	kubectl patch svc orden-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "rl-by-ip\n"}}}'
	kubectl patch svc orden-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-id\n"}}}'
	kubectl patch svc orden-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "cors\n"}}}'
	kubectl patch svc orden-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-termination\n"}}}'
	kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "bot-detection\n"}}}'


    #kubectl create configmap kongconfig --from-file=gateway/conf.d
	#kubectl apply -f gateway/gateway-deploy-ser.yaml

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