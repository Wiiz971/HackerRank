#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here
    Word = sentence.split()
    New = []
    
    for i in Word:
        mot = ""
        mot+=i[0]
        for j in range(len(i)-1):
            if (i[j].lower()<i[j+1].lower()):
                mot += (i[j+1].upper())
            elif(i[j].lower()>i[j+1].lower()):
                mot += i[j+1].lower()
            else:
                mot += i[j+1]
        New.append(mot)
 
    return " ".join(New)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()
