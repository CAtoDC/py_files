# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


con = lite.connect('test.db')

# The 'with' keyword automatically releases the resources
# and provides error handling
with con:
	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')

	data = cur.fetchone()

	print ("SQLite version: %s" % data)
