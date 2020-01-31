kubectl apply -f redis/redis-deploy-ser.yml
kubectl apply -f services/billing/billing-mongo.yml
kubectl apply -f services/client/client-mongo.yml
kubectl apply -f services/fee/fee-mongo.yml
kubectl apply -f services/order/order-mongo.yml