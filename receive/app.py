#!/usr/bin/env python

import json
import logging
import os
import sqlite3
from time import sleep

import pika

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

host = os.getenv('RABBIT_SERVER')
queue = os.getenv('RABBIT_QUEUE')


def insert_values(values):
    """Inserts row into database"""

    conn = sqlite3.connect('/tmp/clicks.db')
    c = conn.cursor()
    c.execute('insert into clicks (email, country, timestamp) values (?, ?, ?)', values)
    conn.commit()
    conn.close()


def callback(ch, method, properties, body):
    """Parses message and calls insert_values"""

    # body received as bytes
    body_as_string = body.decode('utf-8')
    body_as_dct = json.loads(body_as_string)

    email = body_as_dct['email']
    country = body_as_dct['country']
    timestamp = body_as_dct['timestamp']

    insert_values((email, country, timestamp))

    logging.info(f'[x] Received {body_as_string}')


if __name__ == '__main__':

    # need to sleep to give time for rabbit server to start
    sleep(20)

    connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host))
    channel = connection.channel()

    channel.queue_declare(queue=queue)
    channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
