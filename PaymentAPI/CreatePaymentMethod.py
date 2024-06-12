import requests
import json

def createPaymentMethod (cardNumber, exp_month, exp_year, cvc, name, email, contactNumber, addline1, addline2, city, state, postalCode, paymentType):
    url = "https://api.paymongo.com/v1/payment_methods"

    payload = {"data": {"attributes": {
                "details": {
                    "bank_code": "test_bank_one",
                    "card_number": cardNumber,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "cvc": cvc
                },
                "billing": {
                    "address": {
                        "line1": addline1,
                        "line2": addline2,
                        "city": city,
                        "state": state,
                        "postal_code": postalCode,
                        "country": "PH" #Static lang na PH
                    },
                    "name": name,
                    "email": email,
                    "phone": contactNumber
                },
                "type": paymentType
            }}}
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "authorization": "Basic c2tfdGVzdF9YN3Q3M0pQSGpENGlhR2J6eVVxaHFjR0c6"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = json.loads(response.text)

    if response.status_code == 200:
        #pprint.pprint(data)
        response_id = data['data']['id']
        print(response_id)
        return response_id
    else: 
        error = 'Error: ' + data['errors'][0]['code'] + " | " +  data['errors'][0]['detail']
        print(error)
        return error

    print(response.text)

#createPaymentMethod('4120000000000007', 7, 27, '123', 'John Smith', 'test@gmail.com', 'Blk 1 lot 1', 'Santa Rosa', 'Laguna', '4026', 'gcash' )