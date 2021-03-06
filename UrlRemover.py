# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:28:54 2019

@author: ilhamksyuriadi
"""

import xlrd
import re
import xlsxwriter

#Load dataset
data = []
workbook = xlrd.open_workbook("jokowinovember fix.xlsx")#Dataset file name
sheet = workbook.sheet_by_index(0)
for i in range(0,sheet.nrows):
    data.append(str(sheet.cell_value(i,0)))

#remove http and pic.twitter
result = []
for d in data:
    removeHttp = re.sub(r"http\S+", '', d)
    removePic = re.sub(r"pic.twitter\S+", '', removeHttp)
    result.append(removePic)

#file to excel
workbook = xlsxwriter.Workbook('Data(removed url).xlsx')
worksheet = workbook.add_worksheet()
for i in range(len(result)):
    row = 'A' + str(i+1)
    worksheet.write(row,result[i])
workbook.close()