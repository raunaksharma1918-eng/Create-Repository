#Q1.rint numbers from 1 to 10 using a for loop.

# 1Ans:- 
# for i in range(1,11):
#     print(i)


# # Q2. . Print the table of 7 using a loop.
# # 2Ans:-
# for i in range(7,71,7):
#     print(i)


#Q3. . Print all even numbers from 1 to 20.
#3Ans:-

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# Q4. . Find the sum of numbers from 1 to 100
#4Ans:-  

# sum = 0
# for i in range(2,101,2):
#     sum += i
    
# print(sum)

#Q5 . Print all elements of the list: [10, 20, 30, 40, 50].

# nums = [10,20,30,40,50]
# for i in nums:
#     print(i)

#Q6. Print index and value of the list: [5, 10, 15, 20].

# nums = [5,10,15,20]
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])

#Q7. .Count how many elements are in the list [1, 2, 3, 4, 5].

# nums = [1,2,3,4,5]
# print(len(nums))

# #Q8. .. Find the largest number in [12, 45, 7, 89, 23]
# nums = [12,45,7,89,23]
# print(max(nums))



#Q9.. Find the smallest number in [12, 45, 7, 89, 23]

# nums = [12,45,7,89,23]
# print(min(nums))

#Q10. .Count vowels in a string entered by the user.

# text = input("Enter a string: ")

# count = 0

# for ch in text.lower():
#     if ch in "aeiou":
#         count += 1

# print("Number of vowels:", count)

#11. .Create a function that prints 'Hello World'.

# def greet ():
#     print('Hello world')
# greet()

#Q12. .. Create a function that returns the square of a number.



# def square(number):
#     return number * number 
# print(square(5))



#Q13. .Write a function to add two numbers. 

# def add():
#     a = 12
#     b = 14
#     print(a+b)
# add()

#Q14. .Take a number from the user and check if it is even or odd.

# num = int(input("Enter your number"))
# if num % 2 == 0:
#     print('Even number')
# else:
#     print('odd number')

#15. . Take a number from the user and check if it is positive, negative, or zero.

# num = int(input("Enter your number"))
# if num > 0:
#     print("positive number")
# elif num < 0:
#     print("negetive number")
# else:
#     print("zero")

#16. . Print a star pattern of 5 rows.
# for i in range(1,6):
#     print("R" * i)


#17. .Reverse the string 'Python'.
# name = 'python'
# print(name[::-1])

#18. .Count the number of digits in a user-entered number.

# num = input("Enter a number: ")
# print("Number of digits:", len(num))

#19. . Find the factorial of a number using a loop.









#  Q1. Factorial Using Recursion
# Write a Python function to find the factorial of a given number using recursion.
# Sample Input
# Enter number: 5
# Sample Output
# Factorial = 120

# num = int(input('enter your number'))
# square = num * num
# print(square)
# print()

# num = int(input("Enter your number"))
# cube = num * num * num
# print(cube)
# print()

# num1 = int(input("Enter your first number"))
# num2 = int(input("Enter your second number"))
# result = num1 + num2
# print(result)

# num = int(input("Enter your number"))
# result = num / 2
# print(result)


# num1 = int(input("Ener your first number"))
# num2 = int(input("Enter your second number"))
# result = num1 + num2
# print(result)

# num = int(input("Enter your number"))
# result = num * num * num
# print(result)


# num1 = int(input("Ener your first number"))
# num2 = int(input("Enter your second number"))
# result = num1 - num2
# print(result)


# num1 = int(input("Ener your first number"))
# num2 = int(input("Enter your second number"))
# if num1 > num2:
#     print('first number is grateer than')
# else:
#     print('second number is grateer than')




# num = int(input("Enter yor number"))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")



# num = int(input("Enter your number"))
# if num > 0:
#     print("Positive Number")
# else:
#     if num < 0:
#      print("Negative number")
#     else:
#        print("Zero")     


# User se age lo aur check karo ki age 18 ya usse zyada hai to "Eligible", warna "Not Eligible".

# age = int(input("Enter your age"))
# if age >= 18:
#     print("Eligible")
# elif age:
#     print("Not Eligible")



# num = int(input("Enter your number"))
# if num % 5 == 0:
#     print("Divisible")
# else: 
#       print("Not divisible")


# User se ek number lo aur check karo ki wo 10 se bada hai ya nahi.


# num = int(input("Enter your number"))
# if num >= 10:
#     print("Grater than 10")
# elif num < 10:
#     print("Less than and equal to 10")


# User se do numbers lo aur batao dono equal hain ya nahi.

# num1 = int(input("Ener your first number"))
# num2 = int(input("Enter your second number"))
# if num1 == num2:
#     print("both are equal")
# else:
#     print("Both are not eqal")


# User se ek number lo aur check karo ki wo 7 se divisible hai ya nahi.
# num = int(input("Enter your number"))
# if num % 7 == 0:
#     print("Divisible")
# elif num:
#     print("Not divisible")




# User se marks lo.

# Agar marks 40 ya usse zyada hain → "Pass"
# Warna → "Fail"

# num = int(input("Enter your marks"))
# if num >= 40:
#     print("Pass")
# else:
#     print("Fail")


# def add(a,b,c):
#     print(a+b+c)
# add(10,20,30)


# 1 se 20 tak sirf Even numbers print karo.

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)



# 1 se 100 tak jitne bhi numbers hain, unka sum print karo.

# for i in range(1,101):
#     result =  101 + sum
#     print(result)


# num = int(input("Enter your number"))
# result = num * num
# print(result)



# for i in range(1,51):
#     if i % 2:
#         print(i)



# for i in range(1,101):
#     result =  sum =+ sum
#     print(i)



# i = int(input("Enter your number"))
# if i * 10:
#     for i in range(5,51,5):
#         print(i)


# num = int(input("Enter your number"))
# for i in range(1,11):
#     print(num * i)


# num = int(input("Enter your number"))
# for i in range(1,11):
#     print(num, "x", i, "=", num * i)





# num = int(input("Enter your number"))
# for i in range(10,0,-1):
#     print( num, "x", i, "=", num * i)


# def add(*args):
#     total = 0
#     for i in args:
#         return total
    
# print(add(10,20,30,40,50))


# 1 se 50 tak jitne bhi Even numbers hain unka sum print karo.


# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)


# result = 0
# for i in range(1,101):
#     result = result + i
#     print(result)


# User se ek number lo aur uska factorial nikalo

# num = int(input("Enter your number"))
# result = 1
# for i in range(1,num+1):
#     result = result * i
#     print(result)


# num = int(input("Enter your number"))
# result = num * 24
# print(result)

# User se ek number lo aur uska square print karo.

# num = int(input("Enter your number"))
# result = num * num
# print(result)


# ❤️ Ab Question 20 ki baat...
# Agar nahi aata, to koi problem nahi.
# Question 20 (Reverse Number) exam ke hisaab se thoda tough hai.
# Jaise:
# Input:
# 1234
# Output:
# 4321
# Isme while loop aur % operator dono use hote hain.


# a = 1234
# print(end="")
# while a > 0:
# #     digit = a % 10
# #     print(digit,end="")

# d = {
#     "name": "Raunak",
#     "age": 18,
#     "city": "Bhopal"
# }
# print(d.get("items"))


# User se ek number lo aur check karo ki wo 11 se divisible hai ya nahi.

# num = int(input("enter your namber"))
# if num % 11 == 0:
#     print("Divisible")
# else:
#     print("NOt Divisible")


# User se do numbers lo aur unme se bada (greater) number print karo

# num1 = int(input("Enter your first number"))
# num2 = int(input("Enter your second number"))
# if num1 > num2 == 0:
#     print("bada number")

# 1 se 50 tak jitne bhi numbers hain, unme se sirf 5 se divisible numbers print karo.


# for i in range(1,51):
#     if i % 5 == 0:
#         print(i)


# num1 = int(input("Enter your first number"))
# num2 = int(input("Enter your second number"))
# (num1 > num2) and (num2 == 0)
#     print("Grater than first number")
# else:
#     print("Grater thanj second number")


# num1 = int(input("Enter your first number"))
# num2 = int(input("Enter your second number"))
# if num1 > num2:
#     print("First number is Grater")
# else:
#     print("Second number is Grater")


# a = "RAUNAK"
# print(a[3],a[5])

# a = "RAUNAK SHARMA"
# print(a[0:6:1])

# a = "BHUMIHAR"
# print(a[0],a[7])


# a = "hello i am saimtest anlysis"
# print(a[20:27])


# NAME = "RAUNAKSHARM"
# print("MY NAME IS",NAME)

# NAME = "RAUNAKSAHRMA"
# FATHER = "DEVENDRASHARMA"
# AGE = 19
# ADRESS =" BHOPALMADHYAPERDESH"
# print(f"heloo everyone my name is {NAME} and my father name is {FATHER} AND MY AGE IS {AGE} AND I CURRENTLY LIVE IN {ADRESS}")

# print(r'hello my name is raunak shatrma i am from bhihar')

# name = input("What is your namr ?")
# print(f"my name is {name}")

# a = "5"
# b = "4"
# c = a +b
# print(c)

# a = "PYTHON"
# print(a[-1:-7:-1])

# a = "hello"
# print(a[-1:-6:-1])

# X = 10
# X %= 3
# print(X)

# x = 10
# x /= 2
# print(x)

# print(50 * 3)

# print(24 %// 4)

# print(24 // 4 , 24 % 4)
# print(20 //5 , 20 % 5 )
# print(450 % 500) x 100

x = 2 
y = 3
# print(x + y * 2)

# Input a number and print its square.


# num = int(input("Enter your number"))
# result = num * num
# print(result)


# Q2 Input two numbers and print their sum

# num1 = int(input("Enter your firash number:"))
# num2 = int(input("Enter your second number"))
# result = num1 + num2
# print(result)



# Input two numbers and print the greater number

# num1 = int(input("Enter your first number"))
# num2 = int(input("Enter your second number"))
# if num1 > num2 :
#     print("Grater number")
# else:
#     print("Smaller number")


# Check whether a number is even or odd.

# num = int(input("Enter your number"))
# if num % 2 ==0:
#     print("Even number")
# else:
#     print("Odd number") 



# Check whether a number is positive, negative or zero

# num = int(input("Entre your number"))
# if num > 0:
#     print("POsitive")
# elif num < 0:
#     print("Negtaive")
# else:
#     print("zerO")


# Check whether a number is divisible by 11.

# num = int(input("Enter your number"))
# if num % 11 == 0:
#     print("Divisible")
# else: 
#     print("NOt Divisible")


# . Print numbers from 1 to 10.

# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)

#  Print even numbers from 1 to 50

# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)

# Print odd numbers from 1 to 50.

# for i in range(1,51):
#     if i % 2:
#         print(i)


# Print the multiplication table of a given number1

# number1 = int(input("Enter your number"))
# for i in range(1,11):
#     print(f" {number1} x {i} = {number1 * i}")

# . Find the sum of numbers from 1 to 100


# sum = 0

# for i in range(1, 101):
#     sum += i

# print("Sum =", sum)


# Find the factorial of a number

# n = int(input("Enter a number: "))

# result = 1

# for i in range(1, n + 1):
#     result = result * i
#     print(result)

# a = "Raunaksharma"
# print(a[::-1])


# 2) Display three string “Name”, “Is”, “James” as “Name**Is**James”


# A = "Name", "Is", "James"
# print(A)

#  Accept two integers from user and print the sum
#    Ex - The sum of 45 & 12 = 57

# num = int(input("First number grater"))
# num2 = int(input("Second number is grater")) 
# if num > num2 == 0:
#     print("grter number")
# elif num < num2 == 0 :
#     print("low  number")
# else:
#     print("both are equal")


# male = input("Enter name")
# if male :
#     print("Heloo sir")
# elif female:
#     print("HEllo mam")


# num = int(input("Enter your number"))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# age = int(input("Tell your age:- "))
# if age >= 18:
#     print("To aap vote de sakte ho ")
# else:
#     print("aap nhi de sakte ho")



# Day = int(input("aj KITNA TARIK HAI JI"))
# if Day == 1:
#     print("Monday")
# elif Day == 2:
#     print("Tesday")
# elif Day == 3:
#     print("Wednesday")
# elif Day == 4:
#     print("THrusday")
# elif Day == 5:
#     print("Friday")
# elif Day == 6:
#     print("Saturday")
# elif Day == 7:
#     print("Sunday")

# else:
#     print("invalid")


# A = int(input("Enter your first number"))
# B = int(input("Enter your Second number"))
# C = int(input("Enter your Third number"))
# if A >= 


# A = "python programming"
# print(A[0::-1])

# a = "computer"
# print(a[3],a[-1])

# name = "programming"
# print(name[7:11])

# print ming

# num = int(input("Enter your number"))
# Result = num ** num
# print(Result)


