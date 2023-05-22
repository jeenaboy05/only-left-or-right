

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'onlyLeftOrRight' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING input as parameter.

def createString(letters, values):
    string1 = ""
    string2 = ""
    for i in range(0, len(values)):
        if(i==0):
            conditionRight = True
            n = 1
            while(n<len(values) and conditionRight):
                if(values[i]+1==values[n]):
                    string2 = string2 + letters[i]
                    conditionRight = False
                elif(values[i]>values[n]):
                    conditionRight = False
                n=n+1
        elif(i==len(values)-1):
            conditionLeft = True
            n = len(values)-2
            while(n>-1 and conditionLeft):
                if(values[i]+1==values[n]):
                    string1 = string1 + letters[i]
                    conditionLeft = False
                elif(values[i]>values[n]):
                    conditionLeft = False
                n=n-1
        else:
            conditionLeft = True
            conditionRight = True
            temp1 = ""
            temp2 = ""
            n = i-1
            while(n>-1 and conditionLeft):
                if(values[i]+1==values[n]):
                    temp1 = letters[i]
                    conditionLeft = False
                elif(values[i]>values[n]):
                    conditionLeft = False
                n=n-1
            n = i+1
            while(n<len(values) and conditionRight):
                if(values[i]+1==values[n]):
                    temp2 = letters[i]
                    conditionRight = False
                elif(values[i]>values[n]):
                    conditionRight = False
                n=n+1
            if(temp1!=temp2):
                string1 = string1+ temp1
                string2 = string2+temp2
    if(string1=="" and string2 ==""):
        return "NONE"
    elif(string1==""):
        return "NONE " + string2
    elif(string2==""):
        return string1 + " NONE"
    else:
        return string1+" "+string2






def onlyLeftOrRight(input):
    letters = []
    values = []

    # Process each letter in the string
    for letter in input:
        
        if letter not in letters:
            # Find the index where to insert the new letter
            index = 0
            while index < len(letters) and ord(letter) > ord(letters[index]):
                index += 1
            

            # Insert the new letter and assign its value
            letters.insert(index, letter)
            if len(values) == 0:
                value = 0
            elif index == 0:
                value = values[index]+1
            elif index == len(letters) - 1:
                value = values[index - 1] + 1
            else:
                value = max(values[index - 1], values[index]) + 1
            values.insert(index, value)
            
        else:
            # If the letter is already in the array, insert a duplicate and update its value
            index = letters.index(letter)
            letters.insert(index, letter)
            if index == 0:
                value = values[index]+1
            elif index == len(letters) - 1:
                value = values[index - 1] + 1
            else:
                value = max(values[index - 1], values[index]) + 1
            values.insert(index, value)
    print (createString(letters, values))
    
userletters = input("Please enter a string of letters: ")
onlyLeftOrRight(userletters)
