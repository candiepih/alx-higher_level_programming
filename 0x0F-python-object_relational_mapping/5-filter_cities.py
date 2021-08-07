#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all `cities`
    of that state, using the database `hbtn_0e_4_usa`
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    s_name = argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    sql = """SELECT cities.name FROM cities INNER JOIN states
             ON cities.state_id = states.id WHERE states.name = %s
             ORDER BY cities.id ASC"""
    cur.execute(sql, (s_name, ))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    conn.close()
