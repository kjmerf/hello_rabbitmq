#!/usr/bin/env python

import logging
import os
from time import sleep

import pika

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

host = os.getenv('RABBIT_SERVER')
queue = os.getenv('RABBIT_QUEUE')


def callback(ch, method, properties, body):
    """Write messages to file"""

    with open('/tmp/clicks.json', 'ab') as f:
        f.write(body)
        f.write(b'\n')

    logging.info(f'[x] Received {body}')


if __name__ == '__main__':

    # need to sleep to give time for rabbit server to start
    sleep(35)

    # create empty file to which we can append
    with open('/tmp/clicks.json', 'wb') as f:
        pass

    connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host))
    channel = connection.channel()

    channel.queue_declare(queue=queue)
    channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
