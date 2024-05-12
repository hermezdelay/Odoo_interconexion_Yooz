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

Token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJWenhncnBtamdRQkZGbloxdlZaelpPQXBLLVdKU2Q1TmdGWTVKMzBXSjJjIn0.eyJleHAiOjE3MTU1MTUyMTAsImlhdCI6MTcxNTUxMzExMCwianRpIjoiMTEyMTZjMTktNTVlNC00OTNjLWI2YzYtZmZhMDU3YjEzZDVjIiwiaXNzIjoiaHR0cHM6Ly9ldTEuZ2V0eW9vei5jb20vYXV0aC9yZWFsbXMveW9veiIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiIyNjQzMzRiYi0xMTkwLTRiMWEtYjJiNi0xYzZjNDZlMzdjMjciLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ5b296LXB1YmxpYy1hcGkiLCJzZXNzaW9uX3N0YXRlIjoiYjg3YWJlYzAtYzA4My00ZjMxLWFkMGEtZTc1OWI5ZTBiOTNiIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMteW9veiIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MiLCJzaWQiOiJiODdhYmVjMC1jMDgzLTRmMzEtYWQwYS1lNzU5YjllMGI5M2IiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkRhbGlsIEhFUk1FWiIsInByZWZlcnJlZF91c2VybmFtZSI6ImRhbGlsLmhlcm1lekBzeXN0aGVuLmNvbSIsImxvY2FsZSI6ImZyIiwiZ2l2ZW5fbmFtZSI6IkRhbGlsIiwiZmFtaWx5X25hbWUiOiJIRVJNRVoiLCJlbWFpbCI6ImRhbGlsLmhlcm1lekBzeXN0aGVuLmNvbSIsImdyb3VwIjpbXX0.lisCgVJPG9zbDBwyo-6BQMmIbhAoSgcUZH6G6j1xAXfTcET_nSyIxn390WgKoPb5fU7d75B3nuqXDEVEu5Gxt6n5wz7EZD42huBMC2RvOjQ7Y5wVxeb9EZz-OsYu5tkls0P0b53T3gAnMs4JRJuGGDP-9EJOUiUEcOybzXsqJWa0dZl8vWCnZWPl-wH9wRiqu2oLZtOcXsWTT8QMR6hoLZHOWlNkyWU6m316t-L3xuQ7WznlVGABYd0IQ6H8BHcIZMO5468bN_Ut54MJnVaS8gf5JRrgkDE1Sbd7abi2rybhZZvbFYx48oHqTRX8ViID2C3flKvaxXjoweqNljTXO1Bntdqc-6mlSF3yZwlCzcJYiv-zZkiw11AXAQLfdAdVeMe50aEllZrrMxIzwM4re2ZwMMWDahLF5tNFCQbJ22SrUd8onXtHQoxZt6tkEvrJGfy6md1EacS1h0D54YeexNsf0y_nu5q0lQlpqtn9coYeZ4dpbXuznDRrMR8cYAoocWS9NPuUgq52NU6xUVeA1ulYiFQRn_RmHR1ML5QDJHxQlIp1lIzj--Sd-NXPQph5vrM1cCi4lRq8RKzmYbT6iU7JDfPA18sh-t0Am5qXwSSeZPjsjqo4Rs26Un0BTqe-2kLQp5h6jOADaot97F9Ors7R38RWLz7YUcnk0gOMEXI'
authentification_token = connexion_token(url_token, username, password)
Token = 'Bearer '+ authentification_token

headers = {
    'applicationId': '002a61f0-aad5-47b2-b04d-77433f63dcab',
    'Authorization': Token
}
# session.headers.update(my_headers)
response = session.get(url, headers=headers)

print(str(response) + "\n voici la liste des fournisseurs : ")

for element in response.json():
    print(element)

