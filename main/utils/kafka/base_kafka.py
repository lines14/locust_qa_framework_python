import json

from confluent_kafka import KafkaError, Message, Producer

from main.utils.time.time_utils import TimeUtils


class BaseKafka:
    def __init__(
        self,
        bootstrap_servers: str,
        request_event,
        client_id: str | None = None,
    ):
        config = {
            "bootstrap.servers": bootstrap_servers,
        }

        if client_id:
            config["client.id"] = client_id

        self.producer = Producer(config)
        self.request_event = request_event

    def send(
        self,
        topic: str,
        data: dict,
        key: str | None = None,
    ):
        value = json.dumps(data).encode("utf-8")

        start_time = TimeUtils.now_local()
        start_perf_counter = TimeUtils.get_perf_counter()

        def delivery_callback(
            error: KafkaError | None,
            message: Message,
        ):
            response_time = (TimeUtils.get_perf_counter() - start_perf_counter) * 1000

            self.request_event.fire(
                request_type="KAFKA",
                name=topic,
                response_time=response_time,
                response_length=len(value),
                response=message,
                context={},
                exception=error,
                start_time=start_time,
            )

        self.producer.produce(
            topic=topic,
            key=key,
            value=value,
            on_delivery=delivery_callback,
        )

        self.producer.poll(0)

    def flush(self):
        self.producer.flush()
