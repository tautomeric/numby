# -*- coding: utf-8 -*-
"""
Created on Fri May 24 06:35:33 2019

@author: Thomas
"""
import numpy as np
import matplotlib.pyplot as plt

with open("orwell.txt","r") as o:
    data = o.readlines()

line = 2
last_line = len(data)-1

year_means = {}
year_difference = {}
while line<last_line:
    end_line = len(data[line])
    numbers = data[line]
    
    year = int(numbers[end_line-11:end_line-6])
    next_year = int(numbers[end_line-11:end_line-6])
    total = 0
    n = 0
    while year==next_year:
        total = total+float(numbers[end_line-6:end_line-1])
        n = n+1
        line = line+1
        end_line = len(data[line])
        numbers = data[line]
        next_year = int(numbers[end_line-11:end_line-6])
           
    year_means.update({year:(total/n)-50})

new_year = 1931
for i in year_means:
    if i==1931:
        year_difference.update({1931:0})
        continue 
    
    year_difference.update({i:year_means[i]-year_means[new_year]/(i-new_year)})
    new_year= i
       
x, y1 = zip(*sorted(year_means.items()))
x,y2 =  zip(*sorted(year_difference.items()))

plt.figure(1)
plt.bar(x,y1)
plt.title("George Orwell Written Gender By Year")

plt.figure(2)
b = plt.plot(x,y2)
plt.title("Yearly Change In Written Gender")