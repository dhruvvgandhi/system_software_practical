#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#program file and text file both are at same place means in one Folder
import string
text = open("a1.txt", "r") #Open the file in read mode 
a = dict() #Create dictionary
for line in text: #loop through each line of the file 
    line = line.strip() #Remove the leading spaces and newline character 
    line = line.lower() #Convert the characters in line to lowercase to avoid case mismatch 
    line = line.translate(line.maketrans("", "", string.punctuation))# Remove the punctuation marks from the line
    words = line.split(" ") #Split the line into words 
    
    for word in words: #Iterate over each word in line
        if word in a: # #Check word is in dictionary
            a[word] = a[word] + 1 # if word present then Increment count of word by 1 
        else: #if word not present
            a[word] = 1 # then Add the word to dictionary with count 1
        
for key in list(a.keys()):
    print(key, ":", a[key]) #Print dictionary 

