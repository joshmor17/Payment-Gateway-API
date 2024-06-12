import requests
import json

def createPaymentIntent (amount):
    url = "https://api.paymongo.com/v1/payment_intents"

    payload = {"data": {"attributes": {
                "amount": amount,
                "payment_method_allowed": ["card", "paymaya", "gcash"],
                "payment_method_options": {"card": {"request_three_d_secure": "any"}},
                "currency": "PHP",
                "capture_type": "automatic"
            }}}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic c2tfdGVzdF9YN3Q3M0pQSGpENGlhR2J6eVVxaHFjR0c6" #sk_test_X7t73JPHjD4iaGbzyUqhqcGG
    }

    response = requests.post(url, json=payload, headers=headers)
    
    data = json.loads(response.text)

    if response.status_code == 200:
        #pprint.pprint(data)
        paymentIntentID = data['data']['id']
        print(paymentIntentID)
        return paymentIntentID
    else: 
        error = 'Error: ' + data['errors'][0]['code'] + " | " +  data['errors'][0]['detail']
        print(error)
        return error

#createPaymentIntent(10000)