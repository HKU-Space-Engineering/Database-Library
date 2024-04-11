#import 
import xlwings as xw
import FileDealing

D_list= FileDealing.Read("Publisher.txt")

BName = "BOOK.xlsx"
wb = xw.Book(BName)
sht = wb.sheets['sheet1']
A_pos = 'A'
C_pos = 'C'
D_pos = 'D'
F_pos = "F"
G_pos = "G"
pos = 0
ID = 0
#loop
for i in range(2,2321):
    pos = G_pos + str(i)
    sht[pos].value = str(D_list[ID])
    ID += 1
    if (ID >10):
        ID = 0
    print(i)

wb.save(BName)
wb.close()
