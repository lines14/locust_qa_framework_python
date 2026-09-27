from locust import User

from config import Config
from main.utils.kafka.base_kafka import BaseKafka
from main.utils.user.base.base_user import BaseUser


class BaseKafkaUser(BaseUser, User):
    abstract = True

    def __init__(self, environment):
        super().__init__(environment)
        self.config = Config()

        self.kafka = BaseKafka(
            bootstrap_servers=self.config.kafka_url,
            client_id=self.config.CLIENT_ID,
            request_event=environment.events.request,
        )

    def send_transaction(self, topic: str, data: dict):
        self.kafka.send(
            topic=topic,
            data=data,
        )

    def on_stop(self):
        self.kafka.flush()
