#Sets.
"""
empty set -> {}, set()
Values in sets cannot be dublicate.
sets are unorderd or subscriptable.
hetrogenous.
multible.
"""
# s = set()
# print(type(s))


# s = {1,2,3,4,5}
# print(type(s))


# s = {1,1,2,2,3,4,4,5,5}
# print(s)


# s = {1,1,2,2,3,3,4,4,4,5,5}
# print()


# s = {'hello',1,3.14,True}
# print(s)


# #METHODS in sets.

# #1. add a new values in sets.
# #Item Adding 
# s = {1,1,2,2,2,3,3,4,4,5,5}
# s.add(100)
# s.update([200,300,400,500]) #Adding multiple vales inside set.
# print(s)



# #2. Removing an elements from the sets.
# #1. remove(element)
# s = {1,1,1,1,2,2,3,3,3,4,4,5,5}
# s.remove(1)
# print(s)


# s = {1,1,1,1,2,2,3,3,3,4,4,5,5}
# s.discard(6) #agar value exist nahi karti toh it will return you exact set bina kisi error ke 
# print(s)


# s = {1,1,1,1,2,2,3,3,3,4,4,5,5}
# s.clear()
# print(s)


#Advance methods in sets.
"""
1. Union -> sare elements between your stes.
2. Intersection -> Dono set ke beech mai jo common values.
3. symmetric Difference.
4. Difference
"""

s1 = {1,2,3,4,5}
s2 = {1,6,7,8}
print(s1.union(s2))


s1 = {1,2,3,4,5}
s2 = {1,6,7,8}
print(f"Union of set1 and set2 is {s1.union(s2)}")
