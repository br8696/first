import xlwt
def write_xl(row,fields):
    rb=xlrd.open_workbook("student1.xlsx",formatting_info=True)
    r_sheet=rb.sheet_by_index(0)

    wb=copy(rb)
    sheet=wb.get_sheet(0)
    #sheet.write(r,0,fields["name"])
    sheet.write(row,1,fields["attendence"])
    wb.save("stuendt.xlsx")
    print("wrote students.xlsx")
