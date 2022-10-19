import sqlite3

con = sqlite3.connect('local_db_new.db')

cur = con.cursor()

# Create table
table_name = "stock"
query = f"CREATE TABLE if not exists {table_name} (id integer)"
cur.execute(query)

sql_request = '''CREATE TABLE  if not exists stock_0
               (date text, trans text, id real, qty real, price real)'''

cur.execute(sql_request)

# Insert a row of data
cur.execute(f"INSERT INTO stock_0 VALUES ('2008-01-05','BUY','RHAT',100,38.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

for row in cur.execute('SELECT * FROM stock ORDER BY price'):
    print(row)

con.close()
