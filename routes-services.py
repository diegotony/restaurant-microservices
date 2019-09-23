import os
import requests
import json

kongAdmin = ["http://localhost:8001"]
ips = ['http://172.28.1.5:1396']
routesServices = []
with open ('routes.txt') as f:
    routesServices = f.read().splitlines()
    print(routesServices)
# Added Services
for i in kongAdmin:
    for k in ips:
        for m in routesServices:
            response = requests.post(
                '{0}/{1}'.format(i, 'services'),
                data={
                    'name': m,
                    'url': '{0}/{1}'.format(k, m)})
            print(response.status_code)

#  Added Routes
for i in kongAdmin:
    for  l in routesServices:
        response = requests.post('{0}/services/{1}/routes'.format(i,l),data={
            'paths': ['/{0}'.format(l)],
            'methods': ['GET', 'POST', 'PUT', 'DELETE']})
        print(response.status_code)
