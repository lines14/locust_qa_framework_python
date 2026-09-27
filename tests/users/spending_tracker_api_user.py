from locust import task

from main.utils.data.data_utils import DataUtils
from main.utils.data.json_loader import JSONLoader
from main.utils.user.base_api_user import BaseAPIUser
from tests.api.spending_tracker_api import SpendingTrackerAPI


class SpendingTrackerAPIUser(BaseAPIUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        spending_tracker_api = SpendingTrackerAPI()

        response = spending_tracker_api.auth()
        response_body = DataUtils.dict_to_model(response.json())
        self.headers = spending_tracker_api.set_bearer_token(response_body.data)

    @task
    def greetings(self):
        self.client.get(JSONLoader.api_endpoints.spending_tracker.greetings, headers=self.headers)
