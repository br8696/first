import xlrd
for i in range(0,3,1):
    for j in range(0,1,1):
        s=xlrd.open_workbook("student.xlsx","r")
        sh=s.sheet_by_index(0)
        print sh.cell(i,j), sh.cell(i,j+1), sh.cell(i,j+2),"\n"


"""for display all names we have to use loop to display all]

to print onlyname we use print cell.value
"""
    
