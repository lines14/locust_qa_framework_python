from locust import HttpUser, between, events

from config import Config
from main.utils.data.json_loader import JSONLoader
from main.utils.log.logger import Logger
from resources.data.constants import (
    MAX_LOCUST_BETWEEN_USERS_WAIT_TIME,
    MIN_LOCUST_BETWEEN_USERS_WAIT_TIME,
)


class BaseAPIUser(HttpUser):
    abstract = True
    host = Config().base_url

    wait_time = between(
        MIN_LOCUST_BETWEEN_USERS_WAIT_TIME,
        MAX_LOCUST_BETWEEN_USERS_WAIT_TIME,
    )

    @staticmethod
    @events.test_start.add_listener
    def before_all(**_kwargs):
        JSONLoader.load_all()

    @staticmethod
    @events.test_stop.add_listener
    def after_all(**_kwargs):
        Logger.error_log_to_file()
        Logger.log_to_file()

    @staticmethod
    @events.request.add_listener
    def log_request(
        request_type,
        name,  # noqa: ARG004
        response_time,
        response,
        exception,
        url,
        **_kwargs,
    ):
        if exception:
            Logger.error(f"[req] ▶ {request_type}: {url}")
            Logger.error(f"[res]   body: {exception}")
            Logger.error("failed ❌")
        else:
            Logger.log(f"[req] ▶ {request_type}: {url}")
            Logger.log(f"[res]   response time: {response_time}ms")
            Logger.log(f"[res]   status code: {response.status_code}")
            Logger.log("passed ✅")
