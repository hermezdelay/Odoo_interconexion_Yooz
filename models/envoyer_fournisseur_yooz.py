from datetime import timedelta

#from odoo import api, fields, models, _
#from odoo.exceptions import UserError
import logging
import json
import requests
from requests import Session
# from requests.auth import HTTPBasicAuth
# import pandas as pd
# from base64 import b64encode
import array
import json

_logger = logging.getLogger(__name__)


# class chargementFournisseur(models.Model):
#class envoyer_fournisseur_yooz():
    #_inherit = "res.partner"

def envoyer_fournisseur():
    username = "dalil.hermez@systhen.com"
    password = "D@liSec201702"
    # url_fournisseurs = "https://eu1.getyooz.com/yooz/v2/api/YZ_SUPPLIER/referentials"
    # url_fournisseurs = "https://eu1.getyooz.com/yooz/v2/api/YZ_SUPPLIER/referentials/SIEGE/data"
    # url_fournisseurs ="https://preproduction1v2.getyooz.com/yooz/v2/api/YZ_SUPPLIER/referentials/Y/data"
    url_fournisseurs = "https://eu1.getyooz.com/yooz/v2/api/YZ_SUPPLIER/referentials/SIEGE/data"
    url_token = "https://eu1.getyooz.com/auth/realms/yooz/protocol/openid-connect/token"
    # url_token = "https://preproduction1v2.getyooz.com/auth/realms/yooz/protocol/openid-connect/token"

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
        'accept': '*/*',
        'applicationId': '002a61f0-aad5-47b2-b04d-77433f63dcab',
        'Authorization': 'Bearer ' + authentification_token,
        'Content-Type': 'application/json'
    }
    body = ' [ { "data": {"dataBlocks": { "YZ_REFERENTIAL_DATA_COMMONS": {  "YZ_CODE": {  "value": "hermez"   }, "YZ_NAME": {   "value": "hermez"  }  },  "YZ_THIRD_COMMONS": { "YZ_WEB": {  "value": "www.amazon.fr" },  "YZ_SIREN": {  "value": "487773327"  },  "YZ_COUNTRY": { "value": "FR",  "referentialTypeCode": "YZ_COUNTRY",    "referentialCode": "YZ_COUNTRY" },   "YZ_VAT_NUMBER": {  "value": "FR12487773327"  },  "YZ_TAX_VAT_TYPE": {   "value": "DEBIT" }, "YZ_THIRD_ACCOUNT_CODE": {  "value": "4010000" }  }, "YZ_IDENTIFICATION_DATA": { "YZ_WEB": {   "value": "www.amazon.fr" }, "YZ_TOWN": { "page": 1, "value": "Clichy", "position": { "top": 3282.6540833333333, "left": 1064.72125, "right": 1140.266553125, "bottom": 3308.474916666667 }, "setAutomatically": false }, "YZ_SIREN": { "value": "487773327"}, "YZ_COUNTRY": null,"YZ_ADDRESS1": {"value": "AMAZON BUSINESS"}, "YZ_ADDRESS2": {"value": "AMAZON FR"}, "YZ_ZIP_CODE": {"value": "92110"},"YZ_IS_FICTIVE": {"value": false}, "YZ_VAT_NUMBER": { "value": "FR12487773327"},"YZ_FILLING_RATE": {"value": 67 }}, "YZ_ADDRESS": [], "YZ_CONTACT": [],"YZ_BANK": [],"YZ_RESTRICT_VISIBILITY": {"YZ_RESTRICT_VISIBILITY_TO_ORG_UNITS": { "value": []}}, "YZ_ACTIVITY_PERIOD": { "YZ_ACTIVATION_DATE": {"value": "2021-03-11T19:15:43.707Z"},"YZ_INACTIVATION_DATE": {"value": null}}} }}]'

    response = session.put(url_fournisseurs, data=body, headers=headers)
    fournisseur = ""
    """for element in response.json():
        fournisseur = fournisseur + element + " --- "
        web?studio=main#action=349&cids=1&menu_id=522&model=res.partner&view_type=list
        web?studio=main#action=349&cids=1&menu_id=522&model=res.partner&view_type=list
    """
    #print("envoyer le fournisseur : à YOOZ  | " + str(response) + str(response.json() + "sssssss"))
    print("envoyer le fournisseur : à YOOZ  | " + str(response) + "sssssss" + str(response.text()))

    return "envoyer le fournisseur : à YOOZ  | " + str(response) +  "sssssss"




"""
        # recupération des valeurs de champs de la ligne fournisseur
        name = "  name = " + str(self.display_name)
        city = " city = " + str(self.city)
        country = " country = " + str(self.country_id)
        reference = " reference = " + str(self.ref)
        siret = " siret = " + str(self.siret)
        phone = " phone = " + str(self.phone)
        email = " email = " + str(self.email)
        zip = " zip = " + str(self.zip)
        id = " id = " + str(self.id)
"""


"""
        body = [
            {
                "data": {
                    "dataBlocks": {
                        "YZ_REFERENTIAL_DATA_COMMONS": {
                            "YZ_CODE": {
                                "value": "amazon3"
                            },
                            "YZ_NAME": {
                                "value": "AMAZON3"
                            }
                        },
                        "YZ_THIRD_COMMONS": {
                            "YZ_WEB": {
                                "value": "www.amazon.fr"
                            },
                            "YZ_SIREN": {
                                "value": "487773327"
                            },
                            "YZ_COUNTRY": {
                                "value": "FR",
                                "referentialTypeCode": "YZ_COUNTRY",
                                "referentialCode": "YZ_COUNTRY"
                            },
                            "YZ_VAT_NUMBER": {
                                "value": "FR12487773327"
                            },
                            "YZ_TAX_VAT_TYPE": {
                                "value": "DEBIT"
                            },
                            "YZ_THIRD_ACCOUNT_CODE": {
                                "value": "4010000"
                            }
                        },
                        "YZ_IDENTIFICATION_DATA": {
                            "YZ_WEB": {
                                "value": "www.amazon.fr"
                            },
                            "YZ_TOWN": {
                                "page": 1,
                                "value": "Clichy",
                                "position": {
                                    "top": 3282.6540833333333,
                                    "left": 1064.72125,
                                    "right": 1140.266553125,
                                    "bottom": 3308.474916666667
                                },
                                "setAutomatically": false
                            },
                            "YZ_SIREN": {
                                "value": "487773327"
                            },
                            "YZ_COUNTRY": null,
                            "YZ_ADDRESS1": {
                                "value": "AMAZON BUSINESS"
                            },
                            "YZ_ADDRESS2": {
                                "value": "AMAZON FR"
                            },
                            "YZ_ZIP_CODE": {
                                "value": "92110"
                            },
                            "YZ_IS_FICTIVE": {
                                "value": false
                            },
                            "YZ_VAT_NUMBER": {
                                "value": "FR12487773327"
                            },
                            "YZ_FILLING_RATE": {
                                "value": 67
                            }
                        },
                        "YZ_ADDRESS": [],
                        "YZ_CONTACT": [],
                        "YZ_BANK": [],
                        "YZ_RESTRICT_VISIBILITY": {
                            "YZ_RESTRICT_VISIBILITY_TO_ORG_UNITS": {
                                "value": []
                            }
                        },
                        "YZ_ACTIVITY_PERIOD": {
                            "YZ_ACTIVATION_DATE": {
                                "value": "2021-03-11T19:15:43.707Z"
                            },
                            "YZ_INACTIVATION_DATE": {
                                "value": null
                            }
                        }
                    }
                }
            }
        ]

"""

"""        body = {'data': {
                    'dataBlocks': {
                        'YZ_REFERENTIAL_DATA_COMMONS': {
                            'YZ_CODE': {
                                'value': 'SIEGE'
                            }, 
                            'YZ_NAME': {
                                'value': 'SIEGE'
                            }
                        }, 
                        'YZ_THIRD_COMMONS': {'YZ_SIREN': {'value': '335585149'
                            }, 'YZ_SIRET': {'value': '33558514900078'
                            }, 'YZ_COUNTRY': {'value': 'FR', 'referentialTypeCode': 'YZ_COUNTRY', 'referentialCode': 'YZ_COUNTRY'
                            }, 'YZ_VAT_NUMBER': {'value': 'FR57333585149'
                            }, 'YZ_TAX_VAT_TYPE': {'value': 'DEBIT'
                            }
                        }, 
                        'YZ_IDENTIFICATION_DATA': {'YZ_NAME': {'value': 'FRANCE FRAIS'
                            }, 'YZ_TOWN': {'value': 'AULNAT'
                            }, 'YZ_PHONE': {'value': '0473603600'
                            }, 'YZ_SIREN': {'value': '335585149'
                            }, 'YZ_SIRET': {'value': '33558514900078'
                            }, 'YZ_COUNTRY': {'value': 'FR', 'referentialTypeCode': 'YZ_COUNTRY', 'referentialCode': 'YZ_COUNTRY'
                            }, 'YZ_ADDRESS1': {'value': 'ZAC DES RONZIERES'
                            }, 'YZ_ADDRESS2': {'value': 'AVENUE HENRI POURRAT BP 3'
                            }, 'YZ_ZIP_CODE': {'value': '63510'
                            }, 'YZ_IS_FICTIVE': {'value': False
                            }, 'YZ_VAT_NUMBER': {'value': 'FR57333585149'
                            }, 'YZ_FILLING_RATE': {'value': 83
                            }
                        }, 'YZ_ADDRESS': [], 'YZ_CONTACT': [], 'YZ_BANK': [], 
                        'YZ_RESTRICT_VISIBILITY': {
                            'YZ_RESTRICT_VISIBILITY_TO_ORG_UNITS': {'value': []
                        }
                    }, 'YZ_ACTIVITY_PERIOD': {
                            'YZ_ACTIVATION_DATE': {'value': '2021-04-12T18: 20: 34.288Z'
                            }, 
                            'YZ_INACTIVATION_DATE': {
                                'value': None
                            }
                    }
                    }
                }
            }

"""


"""
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
"""

chiane = envoyer_fournisseur()