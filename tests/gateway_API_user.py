from os import getenv
from dotenv import load_dotenv
from API.auth_API import AuthAPI
from locust import HttpUser, task, between
from main.utils.data.JSON_loader import JSONLoader

load_dotenv()

class GatewayAPIUser(HttpUser):
    host = getenv('GATEWAY_URL')
    wait_time = between(
        JSONLoader.config_data.min_wait_time, 
        JSONLoader.config_data.max_wait_time
    )

    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        auth_api = AuthAPI()
        response = auth_api.auth()
        response_body = response.json()
        self.token = response_body['data']['access_token']

    @task
    def get_test_clients(self):
        headers = {"Authorization": f'Bearer {self.token}'}
        self.client.get(JSONLoader.API_endpoints.dictionary.testClients, headers=headers)

    @task
    def get_currency(self):
        headers = {"Authorization": f'Bearer {self.token}'}
        self.client.get(JSONLoader.API_endpoints.dictionary.getCurrency, headers=headers)

    @task
    def get_test_users(self):
        headers = {"Authorization": f'Bearer {self.token}'}
        self.client.get(JSONLoader.API_endpoints.auth.testUsers, headers=headers)
    
    @task
    def get_items(self):
        payload = {
            "methodName": "GetItems",
            "params": {
                "aTableName": "DOCUMENT_TYPE_IDS"
            }
        }

        headers = {"Authorization": f'Bearer {self.token}'}
        self.client.post(JSONLoader.API_endpoints.ESBD.callMethod, json=payload, headers=headers)

    @task
    def get_client(self):
        payload = {
            "methodName": "GetClientByID",
            "params": {
                "aID": "32943107",
                "consent_bool": 1
            }
        }

        headers = {"Authorization": f'Bearer {self.token}'}
        self.client.post(JSONLoader.API_endpoints.ESBD.callMethod, json=payload, headers=headers)

    @task
    def get_agent_list(self):
        payload = {
            "methodName": "GetAgentList"
        }

        headers = {"Authorization": f'Bearer {self.token}'}
        self.client.post(JSONLoader.API_endpoints.ones.callMethod, json=payload, headers=headers)

    @task
    def get_policy(self):
        payload = {
            "methodName": "GetPolicy",
            "params": {
                "num_policy": "206-25-751-0000102"
            }
        }

        headers = {"Authorization": f'Bearer {self.token}'}
        self.client.post(JSONLoader.API_endpoints.ones.callMethod, json=payload, headers=headers)