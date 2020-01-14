

start-clusters:
	kubectl apply -f services/billing/billing-mongo.yml
	kubectl apply -f services/client/client-mongo.yml
	kubectl apply -f services/delivery/delivery-mongo.yml
	kubectl apply -f services/order/order-mongo.yml
	kubectl apply -f services/billing/billing-deploy-ser.yml
	kubectl apply -f services/client/client-deploy-ser.yml
	kubectl apply -f services/delivery/delivery-deploy-ser.yml
	kubectl apply -f services/order/order-deploy-ser.yml


delete-clusters:
	kubectl delete -f services/billing/billing-mongo.yml
	kubectl delete -f services/client/client-mongo.yml
	kubectl delete -f services/delivery/delivery-mongo.yml
	kubectl delete -f services/order/order-mongo.yml
	kubectl delete -f services/billing/billing-deploy-ser.yml
	kubectl delete -f services/client/client-deploy-ser.yml
	kubectl delete -f services/delivery/delivery-deploy-ser.yml
	kubectl delete -f services/order/order-deploy-ser.yml


check:
	kubectl get pods --watch


.PHONY: start-clusters delete-clusters