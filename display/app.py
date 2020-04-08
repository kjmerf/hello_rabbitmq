#! /usr/bin/env python3

from time import sleep

from flask import Flask
from flask import render_template_string

# need to sleep to give time for rabbit server to start
sleep(25)

app = Flask(__name__)


@app.route('/')
def my_form_post():
    """Displays web clicks"""

    with open('/tmp/clicks.json') as f:
        data = f.read().replace('\n', '<br>')

    return render_template_string(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
