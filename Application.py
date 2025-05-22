import openpyxl as xl
wb = xl.load_workbook('test.xlsx')
sheet = wb['Sheet1']
sheet['a1']