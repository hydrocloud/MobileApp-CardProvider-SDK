import requests
import json

APP_PREFIX = "https://app.hydrocloud.net"
#APP_PREFIX = "http://127.0.0.1:5128"
SSO_PREFIX = "https://oneidentity.me"

class CardProvider:
    def __init__(self, service_id, secret_key):
        self.service_id = service_id
        self.secret_key = secret_key
    
    def get_session(self, user_id):
        r = requests.post(SSO_PREFIX + "/services/api/get_token", data = {
            "serviceId": self.service_id,
            "secretKey": self.secret_key
        }).json()
        if r["err"] != 0:
            raise Exception(r["msg"])
        
        svc_token = r["token"]

        r = requests.post(APP_PREFIX + "/api/card_provider/get_session", data = {
            "token": svc_token,
            "user_id": user_id
        }).json()
        if r["err"] != 0:
            raise Exception(r["msg"])
        
        return CardProviderSession(r["token"])

class CardProviderSession:
    def __init__(self, token):
        self.token = token
    
    def add_card(self, title = "", backend_url = "", elements = [], script_code = ""):
        r = requests.post(APP_PREFIX + "/api/card_provider/add_card", data = {
            "token": self.token,
            "card": json.dumps({
                "title": title,
                "backend_url": backend_url,
                "elements": elements,
                "script_code": script_code
            })
        }).json()
        if r["err"] != 0:
            raise Exception(r["msg"])
