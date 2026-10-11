import os

f=open("text.txt","r")

#Read mode
data=f.read
print(data)
line=f.readline()       #used to read data 
print(line)         #used print data
print(type(line))   #used to print type data
f.close()         #used to close file

#Write mode:
f=open("text.txt","a")
f.write("\nI want to eat apple")
f.close()

f=open("sample.txt","w")
f.close()

#r+ mode:overwrite mode:read+overwrite pointer at start,no truncate
f=open("text.txt","r+")
f.write("Abcd")
f.close()

#W+ mode:Truncating mode: read+overwride, truncate
f=open("text.txt","w+")
f.write("Atharv")
print(f.read())
f.close()

#a+:mode:read+append, pointer at end,no truncate 
f=open("Text.txt","a+")
f.write("Hello")
f.close()

#to delete file
os.remove("Sample.txt")




