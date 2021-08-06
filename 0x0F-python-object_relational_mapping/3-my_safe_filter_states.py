#!/usr/bin/python3
""" script that takes in an argument and displays all values in the `states`
    table of `hbtn_0e_0_usa` where `name` matches the argument.
"""
import MySQLdb
from sys import argv

username = argv[1]
password = argv[2]
db_name = argv[3]
s_name = argv[4]
conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=db_name, charset="utf8")
cur = conn.cursor()
sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
cur.execute(sql, (s_name,))
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
