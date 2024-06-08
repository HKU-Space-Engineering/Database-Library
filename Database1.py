#Databae1.py
#It is a python program to link the SQLite3 system

import sqlite3

a = sqlite3.connect("Library_System.db")
print("Success")
print("Print all the information of BOOK table")
result = a.execute("SELECT BOOK_ID,BOOK_TITLE FROM BOOK WHERE BOOK_ID = 10000;")
for i in result:
    print("BOOK_ID = ",i[0])
    print("BOOK_TITLE = ",i[1])
a.close()
