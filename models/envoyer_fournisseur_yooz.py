import datetime
import zeep
from zeep import Client
from zeep.transports import Transport

import requests
from requests import Session
from requests.auth import HTTPBasicAuth
import pandas as pd
from base64 import b64encode
import array
import json


def connexion_token(url_token, username, password):

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    body = {
        'grant_type': 'password',
        'client_id': 'yooz-public-api',
        'username': username,
        'password': password,
        'scope': 'offline_access'
    }

    token = {}
    response = requests.post(url_token,  data=body, headers=headers)
    token = response.json()

    print("token = " + token['access_token'])
    return token['access_token']


username = "dalil.hermez@systhen.com"
password = "D@liSec201702"
url = "https://eu1.getyooz.com/yooz/v2/api/YZ_SUPPLIER/referentials"
url_token = "https://eu1.getyooz.com/auth/realms/yooz/protocol/openid-connect/token"


session = requests.Session()

authentification_token = connexion_token(url_token, username, password)

headers = {
    'applicationId': '002a61f0-aad5-47b2-b04d-77433f63dcab',
    'Authorization': 'Bearer '+ authentification_token
}

response = session.get(url, headers=headers)

print(str(response) + "\n voici la liste des fournisseurs : ")

for element in response.json():
    print(element)

