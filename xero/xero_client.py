import os
from flask import session
import datetime
from xero_python.accounting import AccountingApi
from xero_python.api_client import ApiClient
from xero_python.api_client.configuration import Configuration
from xero_python.api_client.oauth2 import OAuth2Token


class XeroClient:
    def __init__(self, flask_app):
        self.flask_app = flask_app
        self.configuration = Configuration(
            oauth2_token=OAuth2Token(
                client_id=os.getenv('ClientID'),
                client_secret=os.getenv('ClientSecret'),
            ),
            debug=os.getenv('Debug') == 'True'  # Assuming debug is a boolean stored as a string
        )
        self.api_client = ApiClient(self.configuration)
        self.api_client.pool_threads = 1

        # Setup token persistence methods
        self.api_client.oauth2_token_getter(self.obtain_xero_oauth2_token)
        self.api_client.oauth2_token_saver(self.store_xero_oauth2_token)

    def obtain_xero_oauth2_token(self):
        with self.flask_app.app_context():
            return session.get("token")

    def store_xero_oauth2_token(self, token):
        with self.flask_app.app_context():
            session["token"] = token
            session.modified = True

    def get_token(self):
        try:
            # no user auth flow, no exchanging temp code for token
            xero_token = self.api_client.get_client_credentials_token()
        except Exception as e:
            print(e)
            raise
        # todo validate state value
        if xero_token is None or xero_token.get("access_token") is None:
            return "Access denied: response=%s" % xero_token
        self.store_xero_oauth2_token(xero_token)
        return 1

    def get_api_instance(self):
        # Ensure the token is valid before creating an API instance
        self.get_token()
        return self.api_client
