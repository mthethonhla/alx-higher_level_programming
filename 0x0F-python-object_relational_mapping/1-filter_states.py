#!/usr/bin/python3
"""
script that lists all states with a name starting with N
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                        passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    db.close()
