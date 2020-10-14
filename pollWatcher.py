from pandas import *

import numpy as np
import xlwt
import xlsxwriter
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
pollsters=tables[0].find_elements_by_class_name('pollster-container')
pollster_grades=tables[0].find_elements_by_class_name('gradeText')
dates=tables[0].find_elements_by_class_name('date-wrapper')
sample=tables[0].find_elements_by_class_name('sample')
sample_type=tables[0].find_elements_by_css_selector('.sample-type.hide-mobile')
#sample_type=tables[0].find_elements_by_xpath("//*[@class='sample-type' and @class='hide-mobile']")
leader=tables[0].find_elements_by_class_name('leader')
net=tables[0].find_elements_by_class_name('net')
answers=tables[0].find_elements_by_class_name('answers')


#all others 79
print(len(types)) #86
print(len(pollsters))
print(len(pollster_grades)) #76
print(len(dates))
print(len(sample))#80
print(len(sample_type))
print(len(leader))
print(len(net))#80
print(len(answers))


'''workbook=copy(open_workbook('2020_polls.xlsx'))
date=days[0].get_attribute('data-date')
sheet=workbook.add_sheet(date)

for x in range(0,len(types)):
    sheet.write(x,0,date)
    sheet.write(x,1,types[x])
    sheet.write(x,2,pollster[x])
    sheet.write(x,3,dates[x])
    sheet.write(x,1,types[x])
    sheet.write(x,1,types[x])
    sheet.write(x,1,types[x])
    

print(date)

workbook.save('2020_polls.xlsx')
'''

df=DataFrame(columns=["date","pollster","pollster grade", "sample", "sample type", "first", "second", "leader", "net"])
offset=0


for i in range(0,len(dates)):
    print(i)
    print(dates[i].get_attribute('innerHTML'))
    #print(types[i].find_elements_by_css_selector('a')[0].get_attribute('innerHTML'))
    #types[i].find_elements_by_css_selector('a')[0].get_attribute('innerHTML'),
    if len(pollsters[i].find_elements_by_class_name('gradeText'))>0 and i-offset<len(pollster_grades):
        pollster=pollsters[i].find_elements_by_css_selector('a')[1].get_attribute('innerHTML')
        pollster_grade=pollster_grades[i-offset].get_attribute('innerHTML')
    else: 
        pollster=pollsters[i].find_elements_by_css_selector('a')[0].get_attribute('innerHTML')
        pollster_grade="?"
        offset=offset+1
    answer_one=answers[i].find_elements_by_css_selector('p')[0].get_attribute('innerHTML')
    answer_two=answers[i].find_elements_by_css_selector('p')[1].get_attribute('innerHTML')
    print(pollster)
    print(pollster_grade)
    print(sample[i+1].get_attribute('innerHTML'))
    print(sample_type[i].get_attribute('innerHTML'))
    print(answer_one)
    print(answer_two)
    print(leader[i].get_attribute('innerHTML'))
    print(net[i+1].get_attribute('innerHTML'))
    dfNew= DataFrame([[dates[i].get_attribute('innerHTML'),pollster,pollster_grade,sample[i+1].get_attribute('innerHTML'),sample_type[i].get_attribute('innerHTML'), answer_one,answer_two,leader[i].get_attribute('innerHTML'),net[i+1].get_attribute('innerHTML')]],columns=["date","pollster","pollster grade", "sample", "sample type", "first", "second", "leader", "net"])
    #dfNew= DataFrame(np.array([dates[i].get_attribute('innerHTML'),pollster,pollster_grade,sample[i+1].get_attribute('innerHTML'),sample_type[i].get_attribute('innerHTML'), answer_one,answer_two,leader[i].get_attribute('innerHTML'),net[i+1].get_attribute('innerHTML')]))
    print(dfNew)
    df=df.append(dfNew)
print(df)

df.to_excel('2020_polls.xlsx')
with ExcelWriter('2020_polls.xlsx') as writer :
    df.to_excel(writer, sheet_name='since_October_14', index=False, engine='xlsxwriter')
print(df)