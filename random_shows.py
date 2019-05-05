# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:02:55 2019

@author: Thomas
"""
import numpy as np
import matplotlib.pyplot as plt
    
def num_find(doc):
    count = [0,0,0,0,0,0,0,0,0,0]
    with open(doc,"r") as case:
        s = case.readlines()
        doc_lines = len(s)-1
        line_len = len(s[0])
        
        for i in range(doc_lines):
            for j in range(line_len):
                next_char = s[i][j]
                
                if(next_char.isdigit()):
                    count[int(next_char)] = count[int(next_char)]+1

    return count

def by_number(stats):
    for i in range(10):
        print(i,":",abs(stats[i]-100))

numpy_data = np.array(np.random.randint(0,10,1000))
numpy_ran = [0,0,0,0,0,0,0,0,0,0]
for i in numpy_data:
    numpy_ran[i] = numpy_ran[i] + 1
    
true_ran = np.array((num_find("true_ran.txt")))
java_math = np.array((num_find("java_math.txt")))

print("True random:")
by_number(true_ran)
print("std:",np.std(true_ran))

print("\nJava Math Method:")
by_number(java_math)
print("std:",np.std(java_math))

print("\nnumpy.random:")
by_number(numpy_ran)
print("std:",np.std(numpy_ran))

plt.ylabel("Difference from Expected Values on Average")
plt.bar("Java Math",abs(np.mean(java_math)-100))
plt.bar("True Random",abs(np.mean(true_ran)-100))
plt.bar("Numpy Random",abs(np.mean(true_ran)-100))
