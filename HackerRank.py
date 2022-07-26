#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumKeypadClickCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING text as parameter.
#
def get_freq(text):
    freq={}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
            
def sorted_freq_char(text):
    if len(text) <= 9:
        return text
    freq_dic = get_freq(text)
    freq_dic = sorted(freq_dic,key=freq_dic.get,reverse=True)
    return freq_dic        
    

def minimumKeypadClickCount(text):
    print(text)
    sortedchar = sorted_freq_char(text)
    sum = 0
    for i in text:
        if i in sortedchar[0:9]:
            sum+=1
        elif i in sortedchar[9:18]:
            sum+=2
        elif i in sortedchar[18:]:
            sum+=3
    return sum
        
    # Write your code here
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    result = minimumKeypadClickCount(text)

    fptr.write(str(result) + '\n')

    fptr.close()
