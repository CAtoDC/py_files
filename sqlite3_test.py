import sqlite3

# creates db in memory only
createDb = sqlite3.connect(':memory:')

queryCurs = createDb.cursor()

def createTable():
	queryCurs.execute('''CREATE TABLE customers
	(id INTEGER PRIMARY KEY, name TEXT, street TEXT, city TEXT, state TEXT, balance REAL) ''')

def addCust(name, street, city, state, balance):
	queryCurs.execute('''INSERT INTO customers (name, street, city, state, balance)
		VALUES (?,?,?,?,?)''', (name, street, city, state, balance))

def main():
	createTable()

	addCust('Derek Banas', '5708 Highway Ave', 'Verona', 'PA', 150.76)
	addCust('Monty Davis', '1709 First St', 'Irwin', 'PA', 350.60)
	addCust('Paul Smith', '810 Center Ave', 'East Liberty', 'PA', 0.00)
	addCust('Sue Smith', '712 Third St', 'Garfield', 'PA', 50.90)

	createDb.commit()

	# now that we have a db a table and data, query it
	queryCurs.execute('SELECT * FROM customers ORDER BY city')

	for i in queryCurs:
		print ("\n")
		for j in i:
			print (j)

	queryCurs.close()

if __name__ == '__main__': main()
