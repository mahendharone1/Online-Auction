import requests


def sendSMS(contact_no, message):
    import requests

    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contact_no
    headers = {
        'authorization': "knkt8ihCfOKPQ6qkfyVxR0DSNJcB1gNPDdeYHc4jE4g13z4zMa54HzMQOaDB",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    s1=response.text
    return s1
