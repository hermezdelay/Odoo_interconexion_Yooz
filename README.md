# Odoo_interconexion_Yooz

https://{environment}/xyz/v1/api/service/{URIRessource}
xyz here is: "SYSTHEN InvoiceHUB" for me
environment = staging1v2.getyooz.com for technical test and eu1.getyooz.com for production 


By the default the Client ID to use in order to test the public REST API is "yooz-public-api"




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