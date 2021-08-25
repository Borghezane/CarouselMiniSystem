#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importa o modulo de conexao com o mysql
import MySQLdb

db = MySQLdb.connect(host="localhost", user="edison", passwd="edisonSql", db="carrossel")

cursor = db.cursor()


# Teste de insert
# username = input("UserName: ")
# pw       = input("Password: ")

# cursor.execute('INSERT INTO User (username, pass) VALUES (%s,%s)', [username, pw,] )

# db.commit()



# Select
cursor.execute("SELECT id,username FROM carrossel.User")

# posso pegar o número de linhas usando isso
nRows = int(cursor.rowcount)


# for row in cursor.fetchall():	
#    print(str(row[0]) )

remRows = nRows

while( remRows >= 2 ):
	#imprime de 2 em 2
	head_rows = cursor.fetchmany(size=2)
	print("Print duas linhas")
	for row in head_rows:
		print(str(row[0]), str(row[1]))

	remRows -= 2

if( remRows != 0):
	print("Linhas restantes")
	for row in cursor.fetchall():	
	    print(str(row[0]), str(row[1]))

