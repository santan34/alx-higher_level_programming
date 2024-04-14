#!/usr/bin/python3
""" ascript that gets all the states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    stat = cur.fetchall()
    for i in stat:
        print(i)
    cur.close()
    db.close()
