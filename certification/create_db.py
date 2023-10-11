import sqlite3


dbname = 'ipaddress.db'
conn = sqlite3.connect(dbname)



conn.close()
