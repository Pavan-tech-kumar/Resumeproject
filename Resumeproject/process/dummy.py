import requests
import json
url = "https://www.fast2sms.com/dev/bulk"
message="Welcome to otp example using django and fast2sms api"

querystring = {
    "authorization":"ZsN8bVAFhxI24X7THiYz0RW1vfQKjo3GJrldkneuwmBEp9ctgPpFsUyLr6WjGKJmCNAbQS5XiguPZOzI",
    "sender_id":"FSTSMS",
    "message":message,
    "language":"english",
    "route":"p",
    "numbers":"8143545823"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_data=response.text
d1=json.loads(json_data)
if  d1['return']:
    print("Messsage Sent")
else:
    print("Message Not Sent")
