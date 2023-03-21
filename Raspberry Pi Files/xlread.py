import xlrd    
loc = ("D:\Python\py.xlsx")     
wb = xlrd.open_workbook(loc)     
sheet = wb.sheet_by_index(0)     
print(sheet.cell_value(4, 0))  
