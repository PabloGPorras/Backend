from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import os
from ebay.oauthclient.oauth2api import oauth2api
from ebay.oauthclient.credentialutil import credentialutil
from ebay.oauthclient.model.model import environment
from django.http import JsonResponse
import datetime
from ebaysdk.trading import Connection as Trading
from ebaysdk.exception import ConnectionError
from django.shortcuts import redirect

def index(request):
    #EBAY API CONNECTION
    try:
        print('HELLO MATE')
        app_scopes = ["https://api.ebay.com/oauth/api_scope", "https://api.ebay.com/oauth/api_scope/sell.inventory", "https://api.ebay.com/oauth/api_scope/sell.marketing", "https://api.ebay.com/oauth/api_scope/sell.account", "https://api.ebay.com/oauth/api_scope/sell.fulfillment"]

        app_config_path = os.path.join(os.path.split(__file__)[0], 'config', 'ebay-config.json')
        credentialutil_inst = credentialutil
        credentialutil_inst.load(app_config_path)
        oauth2api_inst = oauth2api()
        signin_url = oauth2api_inst.generate_user_authorization_url(credentialutil_inst,environment.PRODUCTION, app_scopes)
        print(f'\n *** test_get_signin_url ***: \n{signin_url}')
        data = {
            'signin_url':signin_url
        }
        return JsonResponse(data)
        
    except ConnectionError as e:
        print(e)
        print(e.response.dict())

def authAccepted(request):
    
    try:
        code = request.GET.get('code')
        print(f"""
        _________________________
        authAccepted code: {code}
        _________________________
        """)
        app_config_path = os.path.join(os.path.split(__file__)[0], 'config', 'ebay-config.json')
        credentialu = credentialutil
        credentialu.load(app_config_path)
        oauth2api_inst = oauth2api()
        user_token = oauth2api_inst.exchange_code_for_access_token(credentialu,environment.PRODUCTION, code)
        print(f"""
        _________________________
        authAccepted user_token: {user_token.access_token}
        authAccepted token_expiry: {user_token.token_expiry}
        authAccepted refresh_token: {user_token.refresh_token}
        authAccepted refresh_token_expiry: {user_token.refresh_token_expiry}
        _________________________
        """)

        #Query String Example: ?strID=XXXX&strName=yyyy&strDate=zzzzz

        response = redirect(f"https://tea-party.vercel.app?accessToken={user_token.access_token}&expiresIn={user_token.token_expiry}&refreshToken={user_token.refresh_token}&refreshTokenExpireIn={user_token.refresh_token_expiry}")
        return response

    except ConnectionError as e:
        print(e)
        print(e.response.dict())


def authDeclined(request):
    try:
        'placeholder'
    except ConnectionError as e:
        print(e)
        print(e.response.dict())



def getUser(request,user_token):
    try:
        app_config_path = os.path.join(os.path.split(__file__)[0], 'config', 'ebay-config.json')
        credentialu = credentialutil
        credentialu.load(app_config_path)
        credential = credentialu.get_credentials(environment.PRODUCTION)
        api = Trading(appid=credential.client_id, devid=credential.dev_id, certid=credential.client_secret, token=user_token.access_token, config_file=None)
        
        response = api.execute('GetUser', {})
        print(response.dict())
        print(response.reply)
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
        

        #GET MEMBER MESSAGES
def getMemberMessages(request,user_token):
    try:
        app_config_path = os.path.join(os.path.split(__file__)[0], 'config', 'ebay-config.json')
        credentialu = credentialutil
        credentialu.load(app_config_path)
        credential = credentialu.get_credentials(environment.PRODUCTION)
        api = Trading(appid=credential.client_id, devid=credential.dev_id, certid=credential.client_secret, token=user_token.access_token, config_file=None)

        now = datetime.datetime.now()

        memberData = {
            "WarningLevel": "High",
            "MailMessageType": "All",
            # "MessageStatus": "Unanswered",
            "StartCreationTime": now - datetime.timedelta(days=120),
            "EndCreationTime": now,
            "Pagination": {
                "EntriesPerPage": "5",
                "PageNumber": "1"
            }
        }

        response = api.execute('GetMemberMessages', memberData)

        print(response.dict())
        print(response.reply)

        if api.response.reply.has_key('MemberMessage'):
            messages = api.response.reply.MemberMessage.MemberMessageExchange

            if type(messages) != list:
                messages = [messages]

            for m in messages:
                print("%s: %s" % (m.CreationDate, m.Question.Subject[:50]))

    except ConnectionError as e:
        print(e)
        print(e.response.dict())


def getOrders(request,user_token):
    try:
        app_config_path = os.path.join(os.path.split(__file__)[0], 'config', 'ebay-config.json')
        credentialu = credentialutil
        credentialu.load(app_config_path)
        credential = credentialu.get_credentials(environment.PRODUCTION)
        api = Trading(appid=credential.client_id, devid=credential.dev_id, certid=credential.client_secret, token=user_token.access_token, config_file=None)

        orders = api.execute('GetOrders', {'NumberOfDays': 30})
        print(orders.dict())
        print(orders.reply)

        data = {
            'orders':orders
        }
        return JsonResponse(data)
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
            
        





 

"""
def mongoDb(request):
    #MONGO DB CONNECTION
    try:
        from pymongo import MongoClient
        username='ebay-django-db'
        password = 'E8KiR0WoJ8IACyKe'
        connect_string  =f'mongodb+srv://{username}:{password}@cluster0.cly8mna.mongodb.net/?retryWrites=true&w=majority'
        my_client = MongoClient(connect_string)
        # First define the database name
        dbname = my_client['ebay']
        # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection)
        collection_name = dbname["ebayitems"]
    except:
        print(e)
        print(e.response.dict())"""
        

        




"""
September Zuriels b-day 
12th through 14th
"""