import requests
import json
#Create a payment for GCash
def CreateAPayment(amount, sourceid):
    
    url = "https://api.paymongo.com/v1/payments"

    payload = {"data": {"attributes": {
                "amount": amount,
                "source": {
                    "id": sourceid,
                    "type": "source"
                },
                "currency": "PHP"
            }}}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic c2tfdGVzdF9YN3Q3M0pQSGpENGlhR2J6eVVxaHFjR0c6"
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)

    if response.status_code == 200:
        resultStatus = result['data']['attributes']['status']
        return resultStatus
    else: 
       errorCode = result['errors'][0]['code']
       errorMessage = result['errors'][0]['detail']

       if errorCode == 'resource_not_chargeable_state':
        resultMessage = errorCode + ": Payment has been failed."
        return resultMessage
       else:
        resultMessage = errorCode + errorMessage
        return resultMessage