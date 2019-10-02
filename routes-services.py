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
            print("Added service /{0} , status: {1}".format(m,response.status_code))

#  Added Routes
for i in kongAdmin:
    for  l in routesServices:
        response = requests.post('{0}/services/{1}/routes'.format(i,l),data={
            'paths': ['/{0}'.format(l)],
            'methods': ['GET', 'POST', 'PUT', 'DELETE']})
        print("Added route /{0} , status: {1}".format(l,response.status_code))


for i in kongAdmin:
    for  l in routesServices:
        response = requests.post('{0}/services/{1}/plugins'.format(i,l),
        data={
            'name':'cors',
            'config.origins':'*',
            'config.methods':'GET',
            'config.methods':'POST',
            'config.methods':'PUT',
            'config.methods':'DELETE',
            'config.headers':'Accept',
            'config.headers':'Accept-Version',
            'config.headers':'Content-Length',
            'config.headers':'Content-MD5',
            'config.headers':'Content-Type',
            'config.headers':'Date',
            'config.headers':'X-Auth-Token',
            'config.exposed_headers':'X-Auth-Token',
            'config.credentials':'true',
            'config.max_age':'3600'
            })
        print("Added cors /{0} , status: {1}".format(l,response.status_code))