from os import getenv
from dotenv import load_dotenv
from main.utils.log.logger import Logger
from locust import HttpUser, events, between
from main.utils.data.JSON_loader import JSONLoader

load_dotenv(override=True)

class BaseAPIUser(HttpUser):
    abstract = True
    host = getenv('BASE_URL')
    wait_time = between(
        JSONLoader.config_data.min_wait_time, 
        JSONLoader.config_data.max_wait_time
    )

    @events.request.add_listener
    def log_request(name, request_type, response_time, response, exception, context, **kwargs):
        if exception:
            Logger.error(f"[req] ▶ {request_type}: {getenv('BASE_URL')}{name}")
            Logger.error(f"[res]   body: {exception}")
            Logger.error("failed ❌")
        else:
            print(f"[req] ▶ {request_type}: {getenv('BASE_URL')}{response.url}")
            print(f"[res]   response time: {response_time}ms")
            print(f"[res]   status code: {response.status_code}")
            print("passed ✅")
