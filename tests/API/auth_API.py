from os import getenv
from dotenv import load_dotenv
from main.utils.log.logger import Logger
from main.utils.API.base_API import BaseAPI
from main.utils.data.JSON_loader import JSONLoader

load_dotenv()

class AuthAPI(BaseAPI):
    login = None
    password = None

    def __init__(self, base_URL=None, log_string=None):
        self.login = getenv('AUTH_LOGIN')
        self.password = getenv('AUTH_PASSWORD')
        super().__init__(
            base_URL or '' or getenv('GATEWAY_URL'), 
            log_string or '[info] ▶ set base API URL'
        )

    def auth(self):
        params = {
            "login": self.login, 
            "password": self.password
        }

        Logger.log(f'[inf]   login as {self.login}:')
        return super().post(JSONLoader.API_endpoints.auth.login, params)