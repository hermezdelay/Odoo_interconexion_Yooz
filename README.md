# Odoo_interconexion_Yooz

https://{environment}/xyz/v1/api/service/{URIRessource}
xyz here is: "SYSTHEN InvoiceHUB" for me
environment = staging1v2.getyooz.com for technical test and 
              eu1.getyooz.com for production 

ApplicationId = gg2d614d-a043-401d-91b7-0220gg32gg87
                (exemple de la documentation)
ApplicationId = 0c830919-fe22-4800-9cea-aa82012a7fda
                (exemple de l'interface API de Yooz)
ApplicationId = 002a61f0-aad5-47b2-b04d-77433f63dcab
                (depuis mon interface d'administration SYSTHEN pour url eu1.getyooz.com)

By the default the Client ID to use in order to test the public REST API is "yooz-public-api"

        In order to use yooz public API you must logged in.
        Oauth2 authentication password grant :
        client_id: yooz-public-api
        client_secret: let empty
        username / password: your session login / password

        Oauth2 authentication grant code :
        client_id: yooz-stats
        client_secret: let empty


At the time, the following data can be synchronized:
- Export files, mainly accounting entries
- Reference/Master data files (org. units, vendors, chart of accounts and cost centers)
- Documents
- Users

API Resources endpoint
The REST API is available in two versions:
1) V1: XML based API which is backward compatible with Yooz V1
2) V2: Enriched JSON based API developed for Yooz Rising


2.1. Yooz Rising endpoints
Yooz resources are published as REST Web Services and are available at the following URL:
https://{environment}/yooz/v2/api/service/{URIRessource}
With:
◼ environment: The environment in which the service is called i.e. .
    EMEA environment
        o eu1.getyooz.com => production
        o preproduction1v2.getyooz.com => pre-production
        o staging1v2.getyooz.com => technical tests
    NORTH AMERICAN environment
        o us1.getyooz.com => production
        o usstaging1.getyooz.com => technical tests
◼ URIRessource: URI of the requested resource (see section 0 below)
        Example:
        https://staging1v2.getyooz.com/yooz/v2/api/orgUnits/

2.2. Yooz V1 backward compatible endpoints
        If you already have a program calling Yooz API and you do not want to adapt your program to the
        new endpoints, you can still use the legacy calls since Yooz Rising is providing backward
        compatibility.
    These legacy resources are published as REST Web Services and are available at the following URL:
    https://{environment}/xyz/v1/api/service/{URIRessource}
        xyz here is: SYSTHEN InvoiceHUB for me,    where xyz is the name of your historical application.
        For instance, if you were calling APIs on an application called “mycompany” on www4 platform like this:
    https://www4.yooz.fr/mycompany/api/service/1/corporates
        You will also be able to call the legacy API using this European URL:
    https://eu1.getyooz.com/mycompany/api/service/1/corporates

NOTE:
The basic HTTP authentication (i.e., a request contains a header field in the form of Authorization:
Basic <credentials>, where credentials is the Base64 encoding of ID and password joined by a single
colon “:”) is not supported anymore by the Yooz Rising JSON APIs but it is still working on the V1
legacy API to assure the backward compatibility to our existing customers.


3 Authentication / Security
    OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It allows Clients to
    verify the identity of the End-User based on the authentication performed by an Authorization
    Server, as well as to obtain basic profile information about the End-User in an interoperable and REST-like manner.

    OpenID Connect allows clients of all types, including Web-based, mobile, and JavaScript clients, to
    request and receive information about authenticated sessions and end-users. 

    There are really two types of use cases when using OpenID Connect (OIDC). The first is an
    application that asks the Yooz server to authenticate a user for them. After a successful login, the
    application will receive an identity token and an access token. The identity token contains
    information about the user such as username, email, and other profile information. The access
    token is digitally signed by the realm and contains access information (like user role mappings) that
    the application can use to determine what resources the user is allowed to access on the application.

    The second type of use cases is that of a client that wants to gain access to remote services. In this
    case, the client asks Yooz to obtain an access token it can use to invoke on other remote services on
    behalf of the user. Yooz authenticates the user then asks the user for consent to grant access to the
    client requesting it. The client then receives the access token. This access token is digitally signed by
    the realm. The client can make REST invocations on remote services using this access token. The
    REST service extracts the access token, verifies the signature of the token, then decides based on
    access information within the token whether or not to process the request

3.1. Client ID
The client ID is a code that will be provided by Yooz in order to access the API. Each Yooz partner or
customer can ask for a particular ID.

By the default the Client ID to use in order to test the public REST API is "yooz-public-api"

    3.1.1. Scopes
    The authentication protocol is based on scopes in order to give you access to a subset of the
    API depending on your contract with Yooz. The available scopes are:

        Scope name                                              Description of permission granted
        create_documents                                        Creating documents on the Yooz application.
                                                                Example: import a new PDF invoice.
        create_feedbacks                                        Creating feedbacks on the Yooz application to
                                                                modify the metadata on a particular document
                                                                i.e. changing the payment date on an invoice.
        manage_referential_data                                 Create, delete or update a master data
                                                                (supplier, analytical plan…)
        read_exports                                            Being able to know if some export files are
                                                                ready et download the exports files available
        manage_organizational_units                             Managing the companies (Create, delete or
                                                                update)
        manage_users                                            Managing users/roles/groups
        Offline_access                                          Obtaining a refresh token which never expires

3.2. Authentication
Yooz Rising API now only supports Oauth2 (bearer) authentication.

    3.2.2. OAuth 2.0 Password grant type
        The password grant is one of the simplest OAuth grants and involves only one step: the application
        presents a traditional username and password login form to collect the user’s credentials and
        makes a POST request to the server to exchange the password for an access token.

    POST -> https://eu1.getyooz.com/auth/realms/yooz/protocol/openid-connect/token
        Authorization : No Auth
        Headers : Content-Type = application/x-www-form-urlencoded
        Body :  grant_type = password
                client_id =  yooz-public-api
                username = dalil.hermez@systhen.com
                password = D@liSec201702
                scope = offline_access   //pour avoie un acces permanent
        Access_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJWenhncnBtamdRQkZGbloxdlZaelpPQXBLLVdKU2Q1TmdGWTVKMzBXSjJjIn0.eyJleHAiOjE3MTUyNjQ2MzksImlhdCI6MTcxNTI2MjUzOSwianRpIjoiMDI1NTJmZDEtNWE4OC00OTQxLTgwZDYtMzgzODcxMzI1NGU3IiwiaXNzIjoiaHR0cHM6Ly9ldTEuZ2V0eW9vei5jb20vYXV0aC9yZWFsbXMveW9veiIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiIyNjQzMzRiYi0xMTkwLTRiMWEtYjJiNi0xYzZjNDZlMzdjMjciLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ5b296LXB1YmxpYy1hcGkiLCJzZXNzaW9uX3N0YXRlIjoiYmU4ZWZjNTItM2Y4NS00NWYyLTgwOGEtMTQyNzlhMjg0Njc4IiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMteW9veiIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MiLCJzaWQiOiJiZThlZmM1Mi0zZjg1LTQ1ZjItODA4YS0xNDI3OWEyODQ2NzgiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkRhbGlsIEhFUk1FWiIsInByZWZlcnJlZF91c2VybmFtZSI6ImRhbGlsLmhlcm1lekBzeXN0aGVuLmNvbSIsImxvY2FsZSI6ImZyIiwiZ2l2ZW5fbmFtZSI6IkRhbGlsIiwiZmFtaWx5X25hbWUiOiJIRVJNRVoiLCJlbWFpbCI6ImRhbGlsLmhlcm1lekBzeXN0aGVuLmNvbSIsImdyb3VwIjpbXX0.unOkQ2pLCLIzuEJTRWU1IBlyixPj4z4hceV9d6t56bkQZ4TUtgL6APjnPBXkx6HS2J17HkDB78inMrDrN92p-06Nf3lefNUZrsq59VCGEJQgOw1Zrh0U6nV0jQ7QWe0tELtWxbU6W0g4vky_ul2f0n5gYFMKynYnROpSlV_PiYqE8SZnfIyl5wyJnPBOfaOPMUuYEeem7JDYQRubbwexS2bxuehQ6ZoYWOL-gNvYVxD8r-eN7MxZWE_SXGHtf5CEwTAseK7mOKQ_ms-e_Sp6hVsGnMTX63PJ2pyP8qQfHA5id_hIkuoMVxA0W7UKZQ3VmtRpO-QJZ0088ofVf4vt3chG8gMI_xssV0WxpMEcNRRG4eIodgRWaDl7duHkBQ4Hi3mmIyB9_S6mcO8dEb6SOi_URlMrctwMfeOvBYPBYI4k3P6brv58ehaCFDsayBLuiacqJo5t55edpej_heaVycl3cFxerS5f4JKJR8lov3r62NNsK2MDm_2dbz9dTmamctDTOHXjdb1moM5s5eCrKY-SdIY9ZUH59f-TJkgVpTYpshOZSJjIpGo1Xfr9qfttf_LTwFLusIXeu_-Ay2dB7E8GjpfAUUoFzP9DT_jLHlnMI_WMBKk-VONvw-qn6B0kJrb-D-gbrBaV0ILZaDVPt5f03PArs2tJmLHnCVfBQWo",

        "expires_in": 2100,
        "refresh_expires_in": 0,
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI4YjNmNzk3NS0yNTQwLTRhM2ItYjNiNy01YWNiNDY0NTQwMmIifQ.eyJpYXQiOjE3MTUyNjI1MzksImp0aSI6IjlkZGFjZTYyLTI0ODgtNDYyOS05YjNhLWRlMDJiM2UwMzdiMiIsImlzcyI6Imh0dHBzOi8vZXUxLmdldHlvb3ouY29tL2F1dGgvcmVhbG1zL3lvb3oiLCJhdWQiOiJodHRwczovL2V1MS5nZXR5b296LmNvbS9hdXRoL3JlYWxtcy95b296Iiwic3ViIjoiMjY0MzM0YmItMTE5MC00YjFhLWIyYjYtMWM2YzQ2ZTM3YzI3IiwidHlwIjoiT2ZmbGluZSIsImF6cCI6Inlvb3otcHVibGljLWFwaSIsInNlc3Npb25fc3RhdGUiOiJiZThlZmM1Mi0zZjg1LTQ1ZjItODA4YS0xNDI3OWEyODQ2NzgiLCJzY29wZSI6InByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MiLCJzaWQiOiJiZThlZmM1Mi0zZjg1LTQ1ZjItODA4YS0xNDI3OWEyODQ2NzgifQ.38w3kwQABdBlkGW_qCkjIVdTbUphGYi0m-Hfsqq92yQ",

3.2.3. Multi-application OAuth 2.0 Password grant (for
partners)
This authentication mode is only available for partners authorized by Yooz on our servers. The
partner must also be authorized to access the customer application. The authorization must be done
by the administrator of the customer application.

