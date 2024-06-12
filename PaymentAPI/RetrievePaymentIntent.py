import requests
import json

def retrievePaymentIntent(paymentIntentID):

    url = "https://api.paymongo.com/v1/payment_intents/" + paymentIntentID

    headers = {
        "accept": "application/json",
        "authorization": "Basic c2tfdGVzdF9YN3Q3M0pQSGpENGlhR2J6eVVxaHFjR0c6"
    }

    response = requests.get(url, headers=headers)

    data = json.loads(response.text)

    if response.status_code == 200:
        status = data['data']['attributes']['status']
        return status
    else: 
        error = 'Error: ' + data['errors'][0]['code'] + " | " +  data['errors'][0]['detail']
        print(error)
        return error