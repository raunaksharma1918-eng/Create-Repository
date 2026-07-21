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



# def multiply(a,b):
#     return a * b
# x = multiply(10 * 5)
# print(x-8)                                   #***********
# multiply()



# def factotial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# print(factotial(5))


# def EvenOdd (a):
#     if a%2 == 0:
#         print('even')
#     else:
#         print('Odd')
# print(EvenOdd(23))


#Some advance function

# def add(a,b,c):
#     print(a+b+c)
# add(10,20,30)


# #*args -> accept argument in form of Tuples.

# def add(*Raunak):
#     print(Raunak)

# add(10,20,30)


# def add(*chacha):
#     sum = 0
#     for i in chacha:
#         print(i)
# add(10,20,30)



# def add(*chacha):
#     sum = 0
#     for i in chacha:
#         sum += i
#         return sum 
# print(add(10,20,30))


# #**kwargs -> dictionary data accept and return 

# def info(**ditials):
#     print(ditials)
# info(name="chacha",age="40",gender="m",address="bhopal",wife='chachi')


# def info(**ditials):
#     for key, value in ditials.items():
#         print(key, value)
# info(name="chacha",age=28,gender="m",address='bhopal')


# """
# Lambda
# """
# add = lambda a,b: a + b
# print(add(10,20))


# #make a lambda function which accepts 2 veriables a=2 and b=2 but give output as a^b 2^2 = 4

# lambda a,b: a**b
# print(power(2,3))

