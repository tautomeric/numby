"""
Counts the percentage occurance of each letter in a writting sample and compares it 
to an expected estimate
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

ave_y = np.array([8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,
                  0.772,4.025,2.406,6.749,7.507,1.929,.095,5.987,6.327,9.056,
                  2.758,.978,2.360,0.150,1.974,.074])

title = input("Title: ")
inpt = input("Writtings: ") 
length = len(inpt)  
    
num_letter = [0 for x in range(26)]
for i in range(length):
    check = ord(inpt[i])
    if 97 <= check <= 122:
        num_letter[check-97]+=1
    elif 65 <= check <= 90:
        num_letter[check-90]+=1
        
y = np.array([x/length*100 for x in num_letter])

ind = np.arange(26) 
width = 0.35      
plt.bar(ind, ave_y, width)
plt.bar(ind + width, y, width)

plt.title(title)

plt.xticks(ind + width / 2, (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']))
label_mine = mpatches.Patch(color = 'orange', label =title)
label_ave = mpatches.Patch(color = 'blue', label='average')
plt.legend(handles=[label_ave,label_mine])
plt.show()
