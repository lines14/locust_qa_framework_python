from config import Config
from main.utils.api.base_api import BaseAPI
from main.utils.data.json_loader import JSONLoader
from main.utils.log.logger import Logger
from resources.data.constants import WAIT_TIME


class SpendingTrackerAPI(BaseAPI):
    def __init__(self):
        self.config = Config()
        super().__init__(self.config.base_url, timeout=WAIT_TIME)

    def auth(self):
        params = {"login": self.config.LOGIN, "password": self.config.PASSWORD}

        Logger.log(f"[inf]   login as {self.config.LOGIN}:")
        return self.post(f"{JSONLoader.api_endpoints.spending_tracker.auth}", params)

    def greetings(self):
        return self.get(f"{JSONLoader.api_endpoints.spending_tracker.greetings}")
