#import 
import xlwings as xw
import random
import FileDealing

loop=0
D_list= FileDealing.Read("namelist.txt")

BName = "BOOK.xlsx"
wb = xw.Book(BName)
sht = wb.sheets['sheet1']
A_pos = 'A'
C_pos = 'C'
D_pos = 'D'
F_pos = "F"
pos = 0
ID = 10000
#loop
for i in range(2,2321):
    pos = C_pos + str(i)
    sht[pos].value = str(D_list[i])
    ID += 1
    print(i)

wb.save(BName)
wb.close()
