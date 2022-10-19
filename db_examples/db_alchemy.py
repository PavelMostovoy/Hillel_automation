import sqlalchemy as alchemy

# with debug
# engine = alchemy.create_engine('sqlite:///local_db_new.db', echo = True)

engine = alchemy.create_engine('sqlite:///local_db_new.db')
connection = engine.connect()

metadata = alchemy.MetaData()

stocks = alchemy.Table('stock', metadata, autoload=True, autoload_with=engine)
stock_0 = alchemy.Table('stock_0', metadata, autoload=True,
                        autoload_with=engine)

# Print the column names

# example for single table
query = alchemy.select(stocks.c.date).filter(stocks.c.qty == 100,
                                             stocks.c.trans == "BUY")

# Generate query
print(query)
print("*" * 20)

query = alchemy.select(stocks.c.date, stock_0.c.date).join(stock_0,
                                                           stocks.c.id ==
                                                           stock_0.c.id)

# print(query)


data = connection.execute(query)
data = data.fetchall()

print(data)

# Print full table metadata
# print(repr(metadata.tables['stock']))
# print(metadata)

query = alchemy.insert(stocks)
values_list = [{'id': '2', 'trans': 'ram', 'qty': 80000, 'price': 12.5},
               {'id': '4', 'trans': 'GHJI', 'qty': 800, 'price': 120.5}]

results = connection.execute(query, values_list)
