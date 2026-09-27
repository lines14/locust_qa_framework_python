from locust import task

from main.utils.user.base_kafka_user import BaseKafkaUser


class SpendingTrackerKafkaUser(BaseKafkaUser):
    @task
    def send_transaction_message(self):
        self.send_transaction(
            topic=self.config.TOPIC_NAME,
            data={
                "user_id": 123,
                "amount": 5000,
                "currency": "KZT",
            },
        )
