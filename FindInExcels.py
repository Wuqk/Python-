import os
import xlrd

def file_name(file_dir):
    for files in os.walk(file_dir):
        return files[2]
def excel():
    #文件夹路径
    path = "D:/Users/Administrator/Desktop/HR"
    L = file_name(path)
    for file in L:
        fname = path+ "/" + file
        wb = xlrd.open_workbook(fname)
        sheetnames = wb.sheet_names()
        for name in sheetnames:
            sheet = wb.sheet_by_name(name)
            for a in range(sheet.nrows):
                cells = sheet.row_values(a)  # 每行数据赋值给cells
                #查找的内容
                if("鲍雯" in cells):
                    print(cells)
                    print("所在文件："+fname+"的第"+str(a)+"行")
excel()
