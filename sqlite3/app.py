#! /usr/bin/env python3

import logging
import sqlite3

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


def main():
    """Creates database file and clicks table"""

    conn = sqlite3.connect('/tmp/clicks.db')
    logging.info('Created database file')

    c = conn.cursor()
    c.execute('create table if not exists clicks (email text, country text, timestamp text)')
    conn.commit()
    logging.info('Created clicks table')
    conn.close()


if __name__ == "__main__":
    main()
