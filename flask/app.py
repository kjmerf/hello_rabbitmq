#! /usr/bin/env python3

import sqlite3
from time import sleep

from flask import Flask
from flask import render_template_string

# need to sleep to give time for rabbit server to start
sleep(25)

app = Flask(__name__)


@app.route('/')
def my_form_post():
    """Displays web clicks"""

    conn = sqlite3.connect('/tmp/clicks.db')
    c = conn.cursor()

    data = ''
    rows = 0
    for row in c.execute('select * from clicks'):
        data += ', '.join(row)
        data += '<br>'
        rows += 1

    conn.close()

    return render_template_string(f'clicks: {rows}<br><br>{data}')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
