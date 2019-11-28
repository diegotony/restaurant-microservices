import argparse
import os
import requests
import json
# help flag provides flag help
# store_true actions stores argument as True

parser = argparse.ArgumentParser()
   
parser.add_argument('--url', required=True)

args = parser.parse_args()





def request_data_json(service,body):
    r = requests.post(url = service,  data = body)
    print(r.text)
    parsed_json=(json.loads(r.text))
    return parsed_json
    # # print(json.dumps(parsed_json, indent=4, sort_keys=True))

def request_data(service,body):
    r = requests.post(url = service,  data = body)
    print(r.text)

if args.url:
    print('Adding to {0} ...'.format(args.url))
    # Added Tables
    request_data('{0}/order/api-order/table'.format(args.url),{'name':"Mesa1"})
    request_data('{0}/order/api-order/table'.format(args.url),{'name':"Mesa2"})
    request_data('{0}/order/api-order/table'.format(args.url),{'name':"Mesa3"})

    # Added Catalog
    almuerzos = request_data_json('{0}/order/api-order/catalog'.format(args.url),{'name':"Almuerzos"})
    desayunos = request_data_json('{0}/order/api-order/catalog'.format(args.url),{'name':"Desayunos"})

    # Added Items

    item1 = request_data_json('{0}/order/api-order/item'.format(args.url),{'name':"Combo 1","description":"Este combo incluye ...","price":2.5,"catalog":desayunos['_id']})
    item2 = request_data_json('{0}/order/api-order/item'.format(args.url),{'name':"Combo 2","description":"Este combo incluye ...","price":3.5,"catalog":desayunos['_id']})

    # Added Users

    user = request_data_json('{0}/client/api-client/users'.format(args.url),{"first_name": "test","last_name": "test","email": "tucotony1396gmail.com","dni": "1150601100","password": "nope"})
   
    print(":3")
