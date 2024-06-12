import requests
import json
import webbrowser
import time

from RetrievePaymentIntent import *


def PaymentIntent(paymentIntendID, paymentMethodID):
    url = "https://api.paymongo.com/v1/payment_intents/" + paymentIntendID + "/attach"

    payload = {"data": 
    {"attributes": {
        "payment_method": paymentMethodID}}}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic c2tfdGVzdF9YN3Q3M0pQSGpENGlhR2J6eVVxaHFjR0c6"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

    data = json.loads(response.text)

    if response.status_code == 200:
        print(data)
        ResultStatus = data['data']['attributes']['status']
        if ResultStatus == 'succeeded': #Dito papasok ang payment if ang ginamit na card is non-3DS or hindi na need ng authentication.
            return ResultStatus
        elif ResultStatus == 'awaiting_next_action': #Dito naman papasok pag ang ginamit na card is 3DS or Need pa ng authentication (E.g. need ng OTP)
            redirectUrl = data['data']['attributes']['next_action']['redirect']['url'] #kukunin yung URL na ibibigay ni paymongo then irerender sa browser.
            webbrowser.open_new(redirectUrl) #mag reredirect sa OTP page or any authentication page. If clinick niyo dun si pass, dapat maging successful yung payment.

            time.sleep(15)
            paymentIntentResult = retrievePaymentIntent(paymentIntendID) #ichecheck ang status ng payment.

            #while paymentIntentResult == 'awaiting_next_action' or paymentIntentResult == 'processing': 
            #paymentIntentResult = retrievePaymentIntent(paymentIntendID)

            if paymentIntentResult == 'succeeded':                                                  
                return paymentIntentResult
            elif paymentIntentResult == 'awaiting_payment_method': #awaiting payment method means failed.
                return 'Payment Failed'
            else:
                return 'Payment Failed'
    else: 
        error = 'Error: ' + data['errors'][0]['code'] + " | " +  data['errors'][0]['detail']
        print(error)
        return error