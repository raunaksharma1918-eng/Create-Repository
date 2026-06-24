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

text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

