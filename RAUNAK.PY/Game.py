# import random

# number = random.randint(1,100) #45

# count = 0
# while count>0: #Infinite Loop
#     count += 1
#     user   = int(input('Enter your number: ')) #45
    
#     if user == number: #user == number, 45 == 45
#         print('You won Man..')
#         print(f"You took {count} to win!")
#         break

#     elif user < number: #21<45
#         print("Too low , Guess high")

#     elif user > number:
#         print('Too high value guess lower value')
        





import random
number=random.randint(1,100)
count=5
while count!=0:
        x=int(input("enter your number:-"))
        count-=1
        if x>number:
            print("your number is high try something your lower!")
            print(f"you have left {count} atttempts!")
        elif x<number:
            print("your number is low try something your higher!")
            print(f"you have left {count} atttempts!")
        else:
             print(f"congrats you have entered the correct number that is {number}")
             break
if count ==0:
     print("you have used all your attempts sorry you lost !!")
print(f"The correct number was {number}")


