# Open Projects
echo "Abriendo Gateway"
cd ~/utpl-thesis-gateway
code .
echo "Abriendo Order"
cd ~/utpl-thesis-order
code .

echo "Abriendo Client"
cd ~/utpl-thesis-client
code .

echo "Levantando Mongo-Rabbit"
cd ~/restaurant-microservices
docker-compose -f docker-compose-dev.yml up -d

