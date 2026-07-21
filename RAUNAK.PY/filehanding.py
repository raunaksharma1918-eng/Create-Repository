"""
operations with a file:
1. r => kisi bhi file ko sirf read kar sakte hai.
2. a => kisi bhi existing content ke last mai new content add kr denge.
3. w -> 1. agar filr exist nhi karti hai toh create kar dega
        2. content daal dega but agar already content exists karta hai file mai toh new se replace.
4.  x -> Create file.
"""



#Reating a file.
# file = open('superman.txt','r')
# print(file.read())



#Using 'w' mode
# file = open('superman.txt','w')
# file.write('this is batman file')
# file.close()



#Using 'a' mode
# file = open('superman,txt','w')
# file.write("This content is added at last.")


# with open('superman.txt','r') as chacha:
#     print(chacha.read())

# with open('batman.txt','w') as chacha:
#     chacha.write('this is batman file')
#     print(chacha.write)


# with open('batman.txt','r') as chacha:
#     print(chacha.read())



#We can remove any file using OS.

import os #Oprating aystem
os.remove('batman.txt')

