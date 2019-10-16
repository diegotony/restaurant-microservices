import yaml
import os
import requests
import json

kong = "http://localhost:8001"
#  load routes file
with open('routes.yml','r') as ymlfile:
    serCfg = yaml.load(ymlfile,Loader=yaml.FullLoader)

with open('api-gateway.yml','r') as ymlfile:
    apCfg = yaml.load(ymlfile,Loader=yaml.FullLoader)


for item , doc in serCfg.items():
    try:
        for route in  doc['routes'] :
            print(route)
            r = requests.post(
            url = "{0}/services".format(kong),  
            data = {
                    'name':"{0}".format(route),
                    'url':"http://{0}:{1}/{2}".format(doc['host'], doc['port'],route )
                    }
            )
            print(r.status_code)

            rr = requests.post(
                url= "{0}/services/{1}/routes".format(kong,route),
                data= {
                    'paths':'/{0}'.format(route),
                    'methods':apCfg['routes']['methods']
                })
            print(rr.status_code)

            rp = requests.post(
                url= "{0}/services/{1}/plugins".format(kong,route),
                data= apCfg['plugins'])
            # print(apCfg['plugins'])
            print(rp.status_code)

            print (route)

        
    except:
        print('error')
        raise