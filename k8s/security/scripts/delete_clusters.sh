kubectl delete -f redis/redis-deploy-ser.yml
kubectl delete -f services/billing/billing-mongo.yml
kubectl delete -f services/client/client-mongo.yml
kubectl delete -f services/fee/fee-mongo.yml
kubectl delete -f services/order/order-mongo.yml