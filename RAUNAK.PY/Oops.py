#When you run your code you always initialize your class
# class Factory:
#     print("hello how are you")

# Factory()
# Factory()  #-> this will not run your code inside class
# Factory()
# Factory()
# Factory()


# class Animal:
#     #attributes
#     a = 12 #a variable defined inside a class is attribute

#     #methods
#     def speak(): #a function defined inside a class is a method
#         print("hello I am Giraffe")

# print(Animal.a)  #calling an attribute
# Animal.speak()   #callling a method

# class Animals:
#     name = "bear"

#     def speak():
#         print("bear is roaling")

# #this is how you create an object 
# obj = Animal()
# obj2 = Animals()  

# #object has all the powers of its class
# print(obj.a) #Objects can also access attributes and methods
# obj.speak()  #here we will send one argument by default 
# print(obj2.a)




# class Bag_factory:

#     def __init__(self):  #self will capture the ,location of object or your class itself
#         print(self)
#         print("hello how are you")

# obj = Bag_factory()
# Bag_factory()  




# class Bag_factory:

#     def __init__(self,meterial,zips,pockets):
#         self.meterial = meterial
#         self.zips = zips
#         self.pockets = pockets

#     def showdetails(self):
#             print("your bag ditial are ")
#             print("Meterials is ",self.meterial)
#             print("toatal zips are ",self.zips)
#             print("total pockets are ",self.pockets)

# campus = Bag_factory("leather",2,4)
# Hrx = Bag_factory("parachute",3,3)
# campus.showdetails()
# Hrx.showdetails()

# print(Hrx.zips)
# print(campus.pockets)





# class Registation:
#     scholl_name = "Sheriyansh"  #class attribute

#     def __init__(self,name,age,email,number):
#          self.name = name              #object attribute / instance attribyutes
#          self.age = age
#          self.email = email
#          self.nuymber = number

#     #objrects methods/ instance method
#     def detialas(self):
#          print("I will not twll you any details")


#     @classmethod
#     def register(cls): 
#          print("you have accesed thr class location")

#     #satatic methods
#     @staticmethod
#     def hello():
#          print("no location is send")



# class register:
#     total_students = 0 #claas attribute
#     def __init___(self,name,age,student_class):
#         self.name = name  #object attribute
#         self.age = age
#         self.cls = student_class
#         self.register = False

#         if self.age > 20:
#             print(f"Regestration Failed : {name}")
#         else:
#             register.total_students += 1
#             print(f"Regestration Succesful : {self.name}")

#      def show_details(self):
#           if self.Registered:
#               print(f"total students -{register.total_students}")
#               print(f"your details are: \n")
#               print(f"name: {self.name}")
#               print(f"age :{self.age}")
#               print(f"class : {self.cls}")
#           else:
#               print(f"sorry no much student exist")
     

# student1 = register("rohan",18,12)
# student2 = register("vikash",22,12)
# student3 = register("harsh"16,10)

# student3.show_detials()



# #OOPS pillars
# #inheritance
# #polymorphism
# #encapsulation
# #abstraction

# class Animal:  # parent class
#     name = "Ape"


#     def speak(self):
#         print(f"{Animal.name} is speaking ")
# class Human(Animal): #child class
#     pass

# obj = Animal()
# obj2 = Human()
# print(obj2.name)
#an objects of your child class can acces all the attribute and
#methods of your parent class



# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


#     def detials(self):
#         print(self.name)
#         print(self.age)


# class Human(Animal):
#     def __init__(self, name, age, mail, number):
#         self.mail = mail
#         self.number = number

#     def ditials(self):   #details method of animals class is now
#         super().ditials()   #overided by human classs details method 
#         print(self.mail)
#         print(self.number)

# class Robot(Human):
#     def __init__(self, name, age, mail, number,chs):
#         super().__init__(name, age, mail, number)
#         self.chs = chs



# obj = Human("Raunak",19,"raunaksharma1918@gmail.com",12343446)
# obj2 = Animal("Giraffe",12)

# obj.detials()
# obj2.detials()


# #HUman class is using the constructor of animal classs 



# class factory:
#     def __init__(self,meteraials):
#         self.meterials = meteraials

# class Factory2:
#     def __init__(self,zips,pockets):
#         self.zips = zips
#         self.pockets = pockets

# class BhopalFactory(Factory2,factory):
#     def __init__(self,meteerials,zips,piockets):
#         Factory.__init__(material)
#         Factory2.__init__(zips.pockets)


#encapsulation
#Access modifiers
#public Attributes and methods
#protector
#private- using _in fromt of any attribute and methods 
          # make them private now no one can access them outside our class


#method overloading = Whenever you have 2 same name methods inside a single class and both have
                     #defferent functional this is know as method overloading


#method overriding = when we have same name methodds inside a parent class and a child class, resulting
                     #you chil class object cannot access thr methods of parent class this concept is of method
                     #overloading


# class Animal:
#     def hello(self,name):
#         print("How are you")

#     def hello(self,name,age):
#         print("What about you")



# class Animal():
#     name = "Lion"
#     __code = "12124dsfdfhdfg132"

#     def speak(self):
#         print(f'{Animal.name}roars')

#     @classmethod
#     def __imei(cls):
#         return cls.__code

# obj = Animal()

# print(obj.__imei())

# obj = Hello("Raunak")
# print(obj.n)


from abc import ABC  , abstractmethod
class Rules(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(Rules):
    def __init__(self,sides):
        self.side = self

    def area(self):
        print(f"area is {self.side*self.side}")

    def perimeter(self):
        print("perimeter is {self.sidde}")

obj = Square(5)





class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"hello you are {self.name} and your age is {self.age}")
    
    def __add__(self,other):
        return self.age + other.age


    
obj = Human("Harsh",23)
obj2 = Human("sarthak",22)
print(obj + obj2) #this will trigger __add__ method
print(obj)  #this will trigger __str__ methods



