#!/usr/bin/python3
"""
    script that lists all `states` from the database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
