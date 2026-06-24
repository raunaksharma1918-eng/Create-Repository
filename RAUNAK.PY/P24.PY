#factorials using recurision.



"""def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))"""


"""n = int(input('Enter the size of list: ')) #5
l = []
for i in range(n): #0,1,2,3,4
    elements = input(f'Enter element {i} for your list: ')
    l.append('element')
print(l)"""



"""num = "rrr"
print(len(num))



name = "ompower"
print(name[4])


name = "ompower"
print(name[::])


name = "ompawer"
print(name[0:5:1])

name = "ompawer"
print(name[2:5])


num = 12
print(type(num))
print(float(num))
print(type(str(num)))
print(bool(num))


num = 12.45
print(int(num))

name = "raunaksharma"
print(str(bool))


boole = True
print(int(boole))


boole = True
print(float(boole))


liste = []
print(bool(liste))


liste = [5,6,7,8,9]
print(bool(liste))


liste = []
print(bool(liste))



a = 45
print(a/2)

a = 45 
print(type(a/2))



a = 13
b = 15 

print(a > b and a >=b )

temperature = int(input("Enter the temprature here: "))
if temperature <= 0:
    print( "freezing cold ")
elif temperature > 0 and temperature <= 10 :
    print("Very Cold")
elif temperature > 10 and temperature <= 20:
    print("Cold")
elif temperature > 20 and temperature <= 30:
    print("pleasent")
elif temperature > 30 and temperature <= 40:
    print("Hot")
else:
    print("Very Hot")"""




#loops (for)******************************************************************

name = ("Raunak")
for i in range(1,101,1):
    print(f"{i}Raunak")

name = ("Raunak")
for i in name:
    print(i)


name = ("Raunaksharma")
print(range(len(name)))


data = "HELLO WORLD"
for i in range(0, len(data) , 2):
    print(i)


data = "HELLO WORLD"
for i in range(0, len(data) , 1):
    print(f"{i} {data[i]}")

#TABLE PRINT*******************************************************************************

for i in range(1 , 11):  
    print(f"2 x {i} = {2 * i}")


#while loops*******************************************************************************

# a = 0
# while a < 10 :
#     print("Hello world") #print unlimited time 


# a = 0
# while a < 10 :
#     a+=a
#     print("Hello world")

data = ""
while data != "Banana":
    data = input("Type Banana' :")

print("you Enterned correctly")
