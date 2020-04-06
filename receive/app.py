#!/usr/bin/env python

import logging
import os
from time import sleep

import pika

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

host = os.getenv('RABBIT_SERVER')
queue = os.getenv('RABBIT_QUEUE')

# need to sleep to give time for rabbit server to start

sleep(35)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host))
channel = connection.channel()

channel.queue_declare(queue=queue)


def callback(ch, method, properties, body):
    logging.info(f'[x] Received {body}')


channel.basic_consume(
    queue=queue, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
