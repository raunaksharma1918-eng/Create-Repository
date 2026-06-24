# 1 list
# 2 dictionary
# 3 tuples
# 4 set 


#1 list 
"""denoted by -> [] square Bracket
1. heterogenous data structure - multiple type ke data ko store larwa sakta hai.

2. Duplicacy is allowed.

3. list is orderd 

4. mutable -> we can change the value  """



""" 1 = [] empty list
l = [10,20,30,40,50]
print(l)
print(type(l))
 

l = [10,20,30,40,50]
l[3] = 400 #Item assignment
print(l)


l = [10,20,30,40,50]

#Item wise loop
for i in l:
    print(i)
 
#Index wise loop 
for i in range(len(l)): #i -> 0,1,2,3,4
    print(i)


for i in range(len(l)): #i -> 0,1,2,3,4
    print(i , l[i])
    #i -> Index of list
    #l[i] -> Item at index


l = [1,67,10,25,14,77]
for i in l:
    if i > 15:
        print(i)


L = [1,67,10,25,14,77]
for i in range (len(L)):
    if L [i] > 15:
        print(i,L[i])


#sum all the elements of the list
l = [10,20,30,40,50]
sum = 0
for i in l:
    sum += i
print(sum)



#slicing
#[start : stop : step] 

# l = [10,20,30,40,50]
#methods in list 


# print()
# input()
# int()"""

"""#1.  . append()  => adding elements at the last of list 
l = [10,20,30,40,50]
l.append(100)
print(l)



#2. .extand()
l1 = [10,20,30,40,50]
l2 = [60,70,80]
l1.extend(l2)
print(l1)

#3. .insert(index,value)
l1.insert(1,100)
print(l1)


#4. .pop(index)
l1 = [10,20,30,40,50]
l1.pop(1)
print(l1)


#5. remove(element)
l1 = [1,2,3,4,5,5,5,5,5]
l1.remove(5) #agar duplicate value hai toh first occurence remove.
print(l1)


#6. len() -> list length
l1 = [1,2,3,4,5,5,5,5,5]
print(len(l1))



#1. Accept list elements and reprint it.
#part1 Accept elements

n = int(input('Enter the size of list: ')) #5
l = []
for i in range(n): #0,1,2,3,4
    elements = input('Enter element for your list: ')
    l.append('element')
print(l)




n = int(input('Enter the size of list: ')) #5
l = []
for i in range(n): #0,1,2,3,4
    elements = input(f'Enter element {i} for your list: ')
    l.append('element')
print(l)          """


#2. Reverse a list without using slicing.

# l = [10,20,30,40,50]
# rev_l = []
# for i in range(len(l)-1,-1,-1):
#     print(l[i])




# 3.print positive and negative elements of an list.
# l = [10,-9,20,30,-12,-15]
# neg = []
# pos = []

# for i in l:
#     if i < 0:
#         neg.append(i)
#     else:
#         pos.append(i)
# print(neg)
# print(pos)


#BUBBLE SORT

# l = [1,5,3,7,4,10]
# for i in l:
#     print(i)
"""
l = [1,5,3,7,4,10]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        pass
    print(l[i],l[j])


    
l = [1,5,3,7,4,10]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
print(l)

"""


# #   0  1  2  3
# l = [10,5,20,15]
# largest = l[0]    #20
# s_largest = l[0]  #10
 
# index = 0  #2
# sindex = 0 #0
# for i in range(len(l)): #i -> 2
#     if l[i] > largest: #20 > 10
#         s_largest = largest
#         largest   = l[i]
#         largest   = l[i]

#         sindex = index
#         index = i
    
#     elif l[i] > s_largest:
#         s_largest = l[i]
#         sindex = i

# print(largest, s_largest)
# print(index, sindex)


"""keys - version Pair
keys cannot ba duplicate
but values can be dupplicate"""


# d = {'a':10, 'b':20, 'c':30, 'd':40}
# #print 40
# print(d['b'])

# #Creating a new key and assigning value to it.
# d['e'] = 100
# print(d)


# d = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 100}
# d['e'] = 200  #old value at key 'e' will be overwrite.
# print(d)

#method in dictionary
#1. .values() -> sirf dictionary ki values.
# info = {'name':'Rahul', 'age':21, 'marks':50.25, 'present': True}
# print(info.values())


# info = {'name':'Rahul', 'age':21, 'marks':50.25, 'present': True}
# info['age'] = 25
# print(info)


# #. .keys() -> sirf keys milengi.
# info = {'name':'Rahul', 'age':21, 'marks':50.25, 'present': True}
# print(info.keys())

#3. .items()
# info = {'name':'Rahul', 'age':21, 'marks':50.25, 'present': True}
# print(info.items())

#4. .pop() -> It accept key and will remove key and values 
# info = {'name':'Rahul', 'age':21, 'marks':50.25, 'present': True}
# info.pop('name')
# print(info)


# info = {'name':'Rahul', 'age':21, 'marks':50.25, 'present': True}
# print(len(info))



info = {'name':'Rahul', 'age':21, 'marks':50.25, 'present': True}
for i in info: #i-> keys
    print(i, info[i]) #info[i] => values


#you will only get values from dictionary.
for i in info.values():
    print(i)


