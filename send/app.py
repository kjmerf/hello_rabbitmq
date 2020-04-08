#!/usr/bin/env python

from datetime import datetime as dt
import json
import os
import logging
import random
from time import sleep

from faker import Faker
import pika

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

host = os.getenv('RABBIT_SERVER')
queue = os.getenv('RABBIT_QUEUE')

faker = Faker()


def publish_click(faker, channel):
    """Publishes fake web clicks to channel"""

    click = {'email': faker.email(), 'country': faker.country(), 'timestamp': dt.today()}
    body = json.dumps(click, default=str)

    channel.basic_publish(exchange='', routing_key=queue, body=body)
    logging.info(f"[x] Sent '{body}'")


if __name__ == '__main__':

    # need to sleep to give time for rabbit server to start
    sleep(30)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host))
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    for x in range(100):
        publish_click(faker, channel)
        sleep(random.randint(0, 5))

    connection.close()
