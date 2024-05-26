from datetime import timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging
import requests
from requests import Session
from requests.auth import HTTPBasicAuth
import pandas as pd
from base64 import b64encode
import array
import json

_logger = logging.getLogger(__name__)


# class chargementFournisseur(models.Model):
class fournisseur_chargement_yooz(models.Model):
    _inherit = "res.partner"

    # la fonction connexion_token() récupére l'acces_token de puis le lien de yooz et le ré-envoie en retour

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
        response = requests.post(url_token, data=body, headers=headers)
        token = response.json()
        print("token = " + token['access_token'])
        return token['access_token']

    def synchronisation_function_yooz(self):
        username = "dalil.hermez@systhen.com"
        password = "D@liSec201702"
        url_fournisseurs = "https://eu1.getyooz.com/yooz/v2/api/YZ_SUPPLIER/referentials"
        url_token = "https://eu1.getyooz.com/auth/realms/yooz/protocol/openid-connect/token"

        session = requests.Session()
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'password',
            'client_id': 'yooz-public-api',
            'username': username,
            'password': password,
            'scope': 'offline_access'
        }
        token = {}
        response = requests.post(url_token, data=body, headers=headers)
        token = response.json()

        authentification_token = token['access_token']
        # authentification_token = self.connexion_token(url_token, username, password)
        headers = {
            'applicationId': '002a61f0-aad5-47b2-b04d-77433f63dcab',
            'Authorization': 'Bearer ' + authentification_token
        }
        response = session.get(url_fournisseurs, headers=headers)
        fournisseur = ""
        for element in response.json():
            fournisseur = fournisseur + element + " --- "

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': "voici la liste des fournisseurs de YOOZ : " + fournisseur + str(response.json()),
                'type': 'success',
                'sticky': False,
            }
        }


"""
    # la fonction connexion_token() récupére l'acces_token de puis le lien de yooz et le ré-envoie en retour
    def connexion_token(self, url_token, mostakhdim, kalima):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'password',
            'client_id': 'yooz-public-api',
            'username': mostakhdim,
            'password': kalima,
            'scope': 'offline_access'
        }
        token = {}
        response = requests.post(url_token,  data=body, headers=headers)
        token = response.json()
        print("token = " + token['access_token'])
        return token['access_token']



    def synchronisation_function_yooz(self):
        return "salam"

        mostakhdim = "dalil.hermez@systhen.com"
        kalima = "D@liSec201702"
        url = "https://eu1.getyooz.com/yooz/v2/api/YZ_SUPPLIER/referentials"
        url_token = "https://eu1.getyooz.com/auth/realms/yooz/protocol/openid-connect/token"


        session = requests.Session()        
        authentification_token = connexion_token(url_token, mostakhdim, kalima)        
        headers = {
            'applicationId': '002a61f0-aad5-47b2-b04d-77433f63dcab',
            'Authorization': 'Bearer '+ authentification_token
        }        
        response = session.get(url, headers=headers)

        print(str(response) + "\n voici la liste des fournisseurs : ")

        for element in response.json():
            print(element)

         return{
        'type':'ir.actions.client',
        'tag':'display_notification',
        'params': {
            'message':  "Parametres envoyés : token bearer" 
            " -----------------------------------> Parametres reçu de Yooz :" + response  ,
            'type': 'success',
            'sticky': False,
            }
        }
  """

