import xlwt
from xlwt import Workbook
from xlutils.copy import copy
from xlrd import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('./chromedriver')
driver.get('https://projects.fivethirtyeight.com/polls/')
driver.implicitly_wait(65)


days=driver.find_elements_by_class_name('day')
tables=driver.find_elements_by_class_name('polls-table')
types=tables[0].find_elements_by_class_name('type')
pollster=tables[0].find_elements_by_class_name('pollster')
dates=tables[0].find_elements_by_class_name('dates')
sample=tables[0].find_elements_by_class_name('sample')
sample_type=tables[0].find_elements_by_class_name('sample-type')
leader=tables[0].find_elements_by_class_name('leader')
net=tables[0].find_elements_by_class_name('net')
answers=tables[0].find_elements_by_class_name('answers')

workbook=copy(open_workbook('2020_polls.xlsx'))
date=days[0].get_attribute('data-date')
sheet=workbook.add_sheet(date)

for x in range(0,len(types)):
    sheet.write(x,0,date)

print(date)

workbook.save('2020_polls.xlsx')