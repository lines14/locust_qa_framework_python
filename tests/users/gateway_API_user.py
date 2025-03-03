from locust import task
from tests.API.auth_API import AuthAPI
from main.utils.data.data_utils import DataUtils
from main.utils.data.JSON_loader import JSONLoader
from main.utils.user.base_API_user import BaseAPIUser

class GatewayAPIUser(BaseAPIUser):
    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        auth_api = AuthAPI()
        response = auth_api.auth()
        response_body = DataUtils.dict_to_model(response.json())
        token = response_body.data.access_token
        self.headers = {"Authorization": f'Bearer {token}'}

    @task
    def get_test_clients(self):
        self.client.get(
            JSONLoader.API_endpoints.dictionary.testClients, 
            headers=self.headers
        )

    @task
    def get_currency(self):
        self.client.get(
            JSONLoader.API_endpoints.dictionary.getCurrency, 
            headers=self.headers
        )

    @task
    def get_test_users(self):
        self.client.get(
            JSONLoader.API_endpoints.auth.testUsers, 
            headers=self.headers
        )
    
    @task
    def get_items(self):
        payload = {
            "methodName": "GetItems",
            "params": {
                "aTableName": "DOCUMENTS_TYPES"
            }
        }

        self.client.post(
            JSONLoader.API_endpoints.ESBD.callMethod, 
            json=payload, 
            headers=self.headers
        )

    @task
    def get_client(self):
        payload = {
            "methodName": "GetClientByID",
            "params": {
                "aID": f"{JSONLoader.test_data.user_id}",
                "consent_bool": 1
            }
        }

        self.client.post(
            JSONLoader.API_endpoints.ESBD.callMethod, 
            json=payload, 
            headers=self.headers
        )

    @task
    def get_agent_list(self):
        payload = {
            "methodName": "GetAgentList"
        }

        self.client.post(
            JSONLoader.API_endpoints.ones.callMethod, 
            json=payload, 
            headers=self.headers
        )

    @task
    def get_policy(self):
        payload = {
            "methodName": "GetPolicy",
            "params": {
                "num_policy": f"{JSONLoader.test_data.num_policy}"
            }
        }

        self.client.post(
            JSONLoader.API_endpoints.ones.callMethod, 
            json=payload, 
            headers=self.headers
        )