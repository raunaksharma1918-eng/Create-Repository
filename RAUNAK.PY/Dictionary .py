#METHOD 1.
""""
data = {}
print(data)


data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
print(data)


data = { "name" : ["raj" , "NIkhil"],      #agar sath me kisi or ka naam likhna hai to [] ye lagana padta hai.
        "age" : 21,
        "Marks" : 89 }
print(data)


data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
print(data["name"])        # kisi 1 value ko print karte hai.
# print(data["raj"])         #Esme error aa jayega 


#METHOD 2 

print(data.get("name"))
print(data.get("raja"))              #or esme None aa jayega 

"""""
""""
data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
data["gender"] = "female"
print(data)


data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
data["gender"] = "female"
print(data)


data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
data["age"] = "19"
print(data)

#Deleted item
#pop()


data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
data.pop("name")   #Esme value ko remove karte hai jaise me name remove ho jayega.
print(data)

"""
#del


data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
del data["age"]         #Esme bhi "age" code kar sab print ho jayega.
print(data)


data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
print(data.keys())
print(data.values())  #Esme sab print ho jayega.
print(data.items())


#loops in dictionary-

data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
for key in data:
    print(key)


data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
for value in data.values():
    print(value)
    

data = { "name" : "raj",
        "age" : 21,
        "Marks" : 89 }
for key, value in data.items():
    print(key,value)                    #Esme sab sath me print ho jayenge.



