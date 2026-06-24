# def add():
#     a = 10
#     b = 20
#     print(a+b)
# add()



# def add(a,b):
#     print(a+b)
# add(10,100)


# def add(a=5,b=15):
#     print(a+b)
# add()


# def multiply():
#     a = 10
#     b = 10
#     print(a * b)
# multiply()



# def info(name,age):
#     print(name,age)
# info("rahul",18)


# #RETURN KEYWARD

# x = info("rahul",18)
# print(x)





# def add(a,b):
#     return a+b
# x = add(15,10)
# print(x-2)



# # def multiply(a,b):
# #     return a * b
# # x = multiply(10 * 5)
# # print(x-8)                                   ***********
# # multiply()



def factotial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(factotial(5))