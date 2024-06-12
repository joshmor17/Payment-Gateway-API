import requests
import json

from CreateAPayment import *

def retrieveASource(sourceid):
    url = "https://api.paymongo.com/v1/sources/src_HQ3TzLKU2VmwoiYCa3neUQrf"

    headers = {
        "accept": "application/json",
        "authorization": "Basic c2tfdGVzdF9YN3Q3M0pQSGpENGlhR2J6eVVxaHFjR0c6"
    }

    response = requests.get(url, headers=headers)

    result = json.loads(response.text)

    if response.status_code == 200:
        resultStatus = result['data']['attributes']['status']
        amount = result['data']['attributes']['amount']
        if resultStatus == 'chargeable': #pending ang status pag failed ang test auth
            CreateAPayment(amount, sourceid)
            return 'Tawagin mo na si create a payment'
        elif resultStatus == 'paid':
            return 'Transaction is already paid'
    else: 
        error = 'Error: ' + result['errors'][0]['code'] + " | " +  result['errors'][0]['detail']
        print(error)
        return error