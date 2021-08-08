#!/usr/bin/python3
"""script that lists all cities from the database `hbtn_0e_4_usa`"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
  username = argv[1]
  password = argv[2]
  db_name = argv[3]


  conn = MySQLdb.connect(host="localhost", port=3306,  user=username,
                         passwd=password, db=db_name,  charset="utf8")
  cur = conn.cursor()
  cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
              INNER JOIN states ON cities.state_id = states.id ORDER
              BY cities.id ASC""")
  rows = cur.fetchall()

  for row in rows:
      print(row)

  cur.close()
  conn.close()
