# sendsms.py

import requests

URL = 'http://91.98.31.210/fullrest/api/send'

headers = { 'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': 'application/json'}

#to = "09120349247"
#message = "02134567"

def make_post_request(to, message):

    data = {'UserName': 'zabix',
            'Password' : 'Aa@123456',
            'Smsbody': message,
            'Mobiles': to,
            "Id" : "0",
            'DomainName': 'sbvd',
            "SenderNumber" : ""
            }
    response = requests.post( url = URL, headers = headers, data = data )
    return response




def send_sms(to, message):
    make_post_request(to, message).json()