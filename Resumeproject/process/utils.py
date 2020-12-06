import requests
import json
from django.core.mail import send_mail
from Resumeproject.settings import EMAIL_HOST_USER

def sendTextMessage(message,contactno):
    url = "https://www.fast2sms.com/dev/bulk"
    querystring = {
        "authorization":"ZsN8bVAFhxI24X7THiYz0RW1vfQKjo3GJrldkneuwmBEp9ctgPpFsUyLr6WjGKJmCNAbQS5XiguPZOzI",
        "sender_id":"FSTSMS",
        "message":message,
        "language":"english",
        "route":"p",
        "numbers":contactno}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data=response.text
    d1=json.loads(json_data)

    return d1['return']
