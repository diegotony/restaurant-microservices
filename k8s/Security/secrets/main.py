import os

def up-dbs():
    os.system("	kubectl apply -f services/billing/billing-mongo.yml")
    os.system("kubectl apply -f services/client/client-mongo.yml")
	os.system("kubectl apply -f services/delivery/delivery-mongo.yml")
	os.system("kubectl apply -f services/order/order-mongo.yml")