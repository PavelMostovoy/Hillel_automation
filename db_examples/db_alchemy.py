import sqlalchemy as db

# with debug
# engine = db.create_engine('sqlite:///local_db.db', echo = True)

engine = db.create_engine('sqlite:///local_db.db')
connection = engine.connect()

metadata = db.MetaData()

stocks = db.Table('stocks', metadata, autoload=True, autoload_with=engine)
secondary = db.Table('secondary', metadata, autoload=True, autoload_with=engine)

# Print the column names

# example for single table
# query = db.select(census.c.date).filter(census.c.qty == 100,
#                                         census.c.trans == "BUY")

query = db.select(stocks.c.date, ).join(secondary,
                                        stocks.c.id == secondary.c.id)

print(query)

data = connection.execute(query)
data = data.fetchall()

print(data)
#
# # Print full table metadata
# print(repr(metadata.tables['stocks']))
#
# #Equivalent to 'SELECT * FROM census'
# query = db.select([census])
# query_1 = db.select([census]).where(census.c.qty == 70)
#
#
# ResultProxy = connection.execute(query_1)
# ResultSet = ResultProxy.fetchall()
# print(ResultSet[:])

print(metadata)
