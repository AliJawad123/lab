# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:26:51 2021

@author: SELAB
"""

def encrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
    
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

def dycryption(text,x):
    result = ""
    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
 
    
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
 
    return result
 
#check the above function
text = "DEFENDTHEFORT"
s = 7
print ("Text  : " + text)
print ("Shift : " + str(s))

print ("Cipher: " + encrypt(text,s))
text2=encrypt(text,s)
print("After dycrypting the encrypted code : ",dycryption(text2,s))


print("JJJJJJJJJJJJJJJJJJJJJ")
print("hello changes")

print("Jawad")
