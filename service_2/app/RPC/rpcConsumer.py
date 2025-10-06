import pika
import json
import os
from dotenv import load_dotenv

load_dotenv()

class Rpc:
    def __init__(self):
        self.params = pika.URLParameters(os.getenv("URL"))
        self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel()

    def QueueDeclareAndBind(self):
        self.channel.exchange_declare(
            exchange=os.getenv("EXCHANGE"), exchange_type="direct", durable=True
        )
        self.channel.queue_declare(queue="summarize_queue", durable=True)
        self.channel.queue_bind(
            queue="summarize_queue",
            exchange=os.getenv("EXCHANGE"),
            routing_key="summarize",
        )

    def callback(self, ch, method, properties, body):
        job = json.loads(body)
        print("Received job:", job)

        result = {"message": "received"}

        # Ensure reply_to exists and is a string
        if properties.reply_to and isinstance(properties.reply_to, str):
            ch.basic_publish(
                exchange="",
                routing_key=str(properties.reply_to),
                properties=pika.BasicProperties(
                    correlation_id=properties.correlation_id
                ),
                body=json.dumps(result),
            )
        else:
            print("Warning: No reply_to queue found for this message!")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consumeMessages(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue="summarize_queue", on_message_callback=self.callback
        )
        print("Consumer is waiting for messages...")
        self.channel.start_consuming()