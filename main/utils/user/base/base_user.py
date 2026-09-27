# main/utils/user/base_user_mixin.py

from locust import between, events

from main.utils.data.json_loader import JSONLoader
from main.utils.log.logger import Logger
from resources.data.constants import (
    MAX_LOCUST_BETWEEN_USERS_WAIT_TIME,
    MIN_LOCUST_BETWEEN_USERS_WAIT_TIME,
)


class BaseUser:
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
    def _log_failed(exception):
        Logger.error(f"[res]   {exception}")
        Logger.error("failed ❌")

    @staticmethod
    def _log_passed(response_time):
        Logger.log(f"[res]   response time: {response_time:.2f}ms")
        Logger.log("passed ✅")

    @staticmethod
    @events.request.add_listener
    def log_request(
        request_type,
        name,
        response_time,
        response,
        exception,
        **kwargs,
    ):
        if request_type == "KAFKA":
            BaseUser._log_kafka_request(
                name=name,
                response_time=response_time,
                response=response,
                exception=exception,
                response_length=kwargs.get("response_length", 0),
            )
            return

        BaseUser._log_http_request(
            request_type=request_type,
            response_time=response_time,
            response=response,
            exception=exception,
            url=kwargs.get("url", name),
        )

    @staticmethod
    def _log_http_request(
        request_type,
        response_time,
        response,
        exception,
        url,
    ):
        if exception:
            Logger.error(f"[req] ▶ {request_type}: {url}")
            BaseUser._log_failed(exception)
        else:
            Logger.log(f"[req] ▶ {request_type}: {url}")
            Logger.log(f"[res]   status code: {response.status_code}")
            BaseUser._log_passed(response_time)

    @staticmethod
    def _log_kafka_request(
        name,
        response_time,
        response,
        exception,
        response_length,
    ):
        if exception:
            Logger.error(f"[req] ▶ KAFKA: {name}")
            BaseUser._log_failed(exception)
        else:
            Logger.log(f"[req] ▶ KAFKA: {name}")
            Logger.log(f"[res]   message size: {response_length} bytes")
            Logger.log(f"[res]   partition: {response.partition()}")
            Logger.log(f"[res]   offset: {response.offset()}")
            BaseUser._log_passed(response_time)
