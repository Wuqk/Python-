import os
import xlrd

"""从多个excel表中查询指定数据所在的excel以及行数"""

#获取文件夹下文件名
def file_name(file_dir):
    for files in os.walk(file_dir):
        return files[2]
def excel():
    #文件夹路径
    path = "D:/Users/Administrator/Desktop/HR"
    L = file_name(path)
    for file in L:
        fname = path+ "/" + file
        #打开excel
        wb = xlrd.open_workbook(fname)
        sheetnames = wb.sheet_names()
        #遍历该excel下的sheet
        for name in sheetnames:
            sheet = wb.sheet_by_name(name)
            for a in range(sheet.nrows):
                cells = sheet.row_values(a)  # 每行数据赋值给cells
                #查找的内容
                if("张三" in cells):
                    print(cells)
                    print("所在文件："+fname+"的第"+str(a)+"行")

if __name__ == '__main__':
    excel()
