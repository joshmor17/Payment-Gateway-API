import requests
import json
import webbrowser

#Create a Source for GCash
#Paymongo Setup https://cynder.atlassian.net/servicedesk/customer/portal/1/topic/ed3737d2-4736-4333-81dd-4062732dd243/article/422215689
def createASource(amount):
    url = "https://api.paymongo.com/v1/sources"

    payload = {"data": {"attributes": {
            "amount": amount,
            "redirect": {
                    "success": "http://localhost:2020/GCash/success.php", #Palitan niyo na lang ng link kung san niyo man ilalagay si success or failed
                    "failed": "http://localhost:2020/GCash/failed.php"
                },
            "type": "gcash",
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
        #pprint.pprint(data)
        redirectURL = result['data']['attributes']['redirect']['checkout_url']
        sourceID = result['data']['id']
        webbrowser.open_new(redirectURL)
        return sourceID
    else: 
       error = 'Error: ' + result['errors'][0]['code'] + " | " +  result['errors'][0]['detail']
       print(error)
       return error
#CreateASource(10000)