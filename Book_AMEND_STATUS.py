#import 
import xlwings as xw
import FileDealing



BName = "RECORD.xlsx"
wb = xw.Book(BName)
sht = wb.sheets['sheet1']
A_pos = 'A'
C_pos = 'C'
D_pos = 'D'
F_pos = "F"
G_pos = "G"
pos = 0
#loop
for i in range(2,111):
    pos = F_pos + str(i)
    if (sht[pos].value == "BORROW"):
        pos = G_pos + str(i)
        sht[pos].value = "N/A" 
    print(i)

wb.save(BName)
wb.close()
