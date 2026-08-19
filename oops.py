## OBJECT ORIENTED PROGRAMMING :- IT IS THE METHOD OF PROGRAMMING USING WHICH WE DEVELOP A DESIGN AROUND WHICH OUR INSTANCES(OBJECTS)
##                                BOUNDED .SIMPLY SPEAKING WE ARE DEVELOPING A CODE AROUND WHICH OUR DATA WILL BE BOUNDED.


################################################################################################################
# class PlayerCharacter:
#     membership= True #GLOBAL ATTRIBUTE OF PLAYER CLASS ALSO KNOWN AS CLASS ATTRIBUTE. ( ATTRIBUTES = PROPERTIES )
#     def __init__(self,name,age,city="not known"):  #1. "self" keyword means the reference to the class ( self = class_itself )AND
#         self.name=name                             #2.  '__init__()' function is a constructor used to construct the object of classes
#         self.age=age # LOCAL ATTRIBUTES OF PLAYER CLASS OR KNOWN AS OBJECT ATTRIBUTES 
#         self.city=city   
#     def age_verify(self):  
#         if (self.age>18):
#             return "major"
#         return "minor"

# class Archer(PlayerCharacter):
#     def __init__(self, name, age, city="not known"):
#         super().__init__(name, age, city) #1.WHILE INHERITING FROM PARENT CLASS, CHILD CLASS ONLY INHERITS GLOBAL ATTRIBUTES BY DEFAULT THUS
#     def power(self,power):                #2.TO INHERIT LOCAL ATTRIBUTES FROM PARENTS CLASS SUPER FUNCTION IS USED. BUT THIS IS NOT THE CASE
#         self.power=power                  #3.WITH METHODS, WHILE INHERITING FROM PARENT CLASS CHILD CLASS ALSO INHERITS ALL OF ITS METHODS.
        

# emp1=PlayerCharacter("Kabeer",21)     
# print(emp1.membership)
# print(emp1.age_verify())
# emp2=Archer("kzif",13,"venice")
# print(emp2.age_verify()) 
# print(emp2.membership)
# ################################################################################################################

### ABSTRACTION:-bstraction is the hiding of the functionalities of the methods that manipulate the data,this feature
#                brings more efficiency as sometimes without knowing how any method or funtion works we would rather 
#                use its functionality.

##------------------------------------------------------------------------------------------------------------

# from abc import ABC,abstractmethod
# class PlayerChar(ABC):#ABSTRACT CLASS 
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     @abstractmethod #this decorator is used to abstract the methods within the class from subclasses or other classes 
#     def age_check(self):
#         if(self.age<=18):
#             print("you're a minor")
#         else:
#             print("you're eligible for playing game")     
#     def new_age_check(self):
#         if(self.age<=10):
#             print("exit immediately you're a child") 
#         else :
#             print("you can still play game but of only child ones")              

# class Idle(PlayerChar):#CHILD CLASS OF ABSTRACT CLASS (CONCRETE CLASS OR REGULAR CLASS)
#     def __init__(self, name, age):
#         super().__init__(name, age)    
#     def age_check(self):
#         return super().age_check()
        
# # player0=PlayerChar('kaushal',18)  #this will show error as we cannot create a instance of abstract class         
# player1=Idle("kabeer",20) #this will not show error as there is 
# player1.age_check()
# player1.new_age_check()
##------------------------------------------------------------------------------------------------------------

# NOTE:- 1) Percentage of Abstraction in any abstracted class can be calculated using formula -  
#           % of abstraction in class = (number of methods created using abstract method)/(total number of methods in that class) 
#        2) we cannot create a object of an abstracted class and thus also cannot directly use its methods , inorder to create a 
#           object of an abstracted class we create a subclass of that abstracted class and then access the regular methods of
#           abstracted class .
#        4) we cannot directly use the abstracted methods of abstracted class even after using object of subclasses of abstracted class
#           thus we create a method in subclass and call the desired abstract method of abstract class using super() function .
#        5) we can directly call the regular methods or concrete methods of abstracted class using subclasses.

######################################################################################################################################


# INHERITENCE:- it is the dependency of the subclasses to the parent class in various fashion. Such as:-
#                a)Heirarchial class inheritence 
#                b)Multilevel class inheritence 
#                c)Multiple class inheritence
#                d)Hybrid class inheritence 
#                e)Single class inheritence

#########################################################################################
##MULTIPLE INHEERITENCE -
# class Employee:
#    pass
# class Company:
#    pass
# class EmployeeDetails(Employee,Company):##THIS IS THE PARTICULAR OF MULTIPLE INHERITENCE
#     pass
#########################################################################################
##SINGLE CLASS INHERITENCE-

# class Employee:
#    pass
# class Company(Employee):
#    pass
#########################################################################################
##HIERARCHICAL CLASS INHERITENCE -

# class A:
#     pass
# class B(A):
#     pass 
# class C(A):
#     pass 
#########################################################################################
##HYBRID CLASS IHERITENCE-

# class A:
#     pass
# class B:
#     pass
# class C(B,A):##MULTIPLE INHERITENCE
#     pass
# class D(A):##SINGLE INHERITENCE
#     pass
# class E(D):##MULTILEVEL INHERITENCE
#     pass 
##########################################################################################
##MULTILEVEL CLASS INHERTENCE-

# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
#########################################################################################

##################################################################################################################
## CLASS OBJECT ATTRIBUTE WHICH INSTANTIATES THE GLOBAL ATTRIBUTES WITHIN THE CLASS WHICH IS ACCESSIBLE BY ALL INSTANCES CREATED USING 
## THE SAME CLASS OR CHILD CLASS OF THE SAME PARENT CLASS UNDER WHICH CLASS OBJECT ATTRIBUTE IS DEFINED WE HAVE SIMILIAR CONCEPT FOR METHODS.
##                          THAT IS CREATING A METHOD WHICH IS ACCESIBLE BY ALL OF ITS INSTANCES WITHOUT THE DECLARATION OF ACTUAL INSTANCE.
##------------------------------------------------------------------------------------------------------------

# class PetShop:
#     animal=True
#     def __init__(self,name,cage_no,type):
#         self.name=name
#         self.cage_no=cage_no
#         self.type=type
# class Cat(PetShop):
#     def __init__(self, name, cage_no, type):
#         super().__init__(name, cage_no, type)
#     def discount_verify(self):
#         if(self.type=="cat" or self.type=="CAT" or self.type=="Cat"):
#             return "valid for discount"       
#         return "not valid for discount" 

      #CLASS METHOD:- decorator is used to create method for a class and call it without use of object of that class ,using independant value
#     @classmethod 
#     def food_avail(cls,cage_no): ##here we can see that there is no need of creating an instance to use the food_avail method  
#         if (cage_no>5):
#             return "food is available"        
#         return "food not available"

      #STATIC METHOD:-is as same as class method but we don't need to pass any cls command for it (cls refer to class refrence )
#     @staticmethod
#     def cleaning(cage_no):
#         if(cage_no>10):
#             return "no need to clean "
#         return "cleaning will be done shortly"
# print(Cat.food_avail(1)) 
# print(Cat.cleaning(12))   
###################################################################################################################



##########################################################################################################
###METHOD RESOLUTION ORDER (MRO) : This is the order in which the methods will be called in case of multiple inheritance or hybrid inheritance or multilevel inheritance
##------------------------------------------------------------------------------------------------------------ 
##CASE 1:
# class A():
#     num=1
# class B(A):
#     num=2
# class C(A):  
#     num=3
# class D(B,C):
#     num=4
# m=D()
# print(m.num)#this will print the value of num according to the order of inheritance
# print(D.mro())#this will print the order in which the methods will be called  
# ## HERE MRO IS D->B->C->A
##------------------------------------------------------------------------------------------------------------
##CASE 2:
# class A():
#     def process(self):
#         print('A process')
# class B(A):
#     def process(self):
#         print('B process')
# class C(A,B):
#     def process(self):
#         print('C process')
# obj=C()
# obj.process()#This will give out the error as THE MRO is C->A->B->A but problem asrises with the good head rule that is 
# ##            A is a superclass of B and cannot be called before calling B but the order of MRO Is C->A->B->A and hence it will give out an error
# ##            hence to solve this problem we need to use super() function in the class C and call the process method of class A
####################################################################################################################################




################################################################################################################
###DUNDER METHODS :- THEY ARE ALSO KNOWN AS MAGIC METHODS THAT ARE PREDEFINED IN THE PYTHON WHICH GENERALLY SHOULDN'T BE CHANGED 
#                    BUT CAN SOMETIMES BE MODIFIED IN SOME SPECIAL CASE .

##------------------------------------------------------------------------------------------------------------
##1.
# class Expo:
#     def __init__(self,name):
#         self.name=name
 
# new_vehicle=Expo("car")
# print(str(new_vehicle)) ##below command will also print the same result as that of this line 
# print(new_vehicle.__str__())##we can also observe that the dunder methods can be used as the functions as well as methods
# print(type(new_vehicle))
##------------------------------------------------------------------------------------------------------------
##2.
# class SuperList(list):
#     def __len__(self):
#         return super().__len__()     ##this is a example how predefined functions in python works for differenet objects
    
# list1=SuperList((1,2,3,4))   #here we are passing set instead of list
# print(len(list1)) 
##------------------------------------------------------------------------------------------------------------
##3.
# class NewList(list):
#     def __append__(self,value):
#         return self.extend(num for num in value)
# list2=NewList([1,2,34])
# list3=list2.copy()
# list2.__append__([1,2,3,4,67]) ## here we modified the append method with the help of special magic method and had made it functional 
# list3.extend([1,2,3,4,67])     ## like extend method
# print(list3)
# print(list2)
##------------------------------------------------------------------------------------------------------------
##4.
# print(str("hello"))
# class NewEmp:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f'{self.name}'    
# some_emp=NewEmp("kabbu")
# print(str(some_emp))   ##due to polymorphism the function 'str' is behaving diffenently with different objects 
# print(some_emp.__str__()) 
# print(str("hello"))
##------------------------------------------------------------------------------------------------------------
##5.COMPARE THIS CASE WITH ABOVE EXAMPLE AND CONCLUDE
# class NewEmp:
#     def __init__(self,name):
#         self.name=name
# some_emp=NewEmp("NOPLAYER ")
# print(str(some_emp))
# print(some_emp.__str__())        
################################################################################################################



################################################################################################################

##DECORATOR:- A decorator is fundamentally a function that takes another function as an argument and returns a new function,
##.           which typically wraps the original function to modify its behavior.

##------------------------------------------------------------------------------------------------------------
##1.BASIC STRUCTURES OF HOW PYTHON DECORATORS WORKS 
# def decorator(func):
#     def wrap_func(*x):
#         print("*"*8)        ##this is the design of how the decorator will modify our base function or module 
#         func(*x)
#         print("*"*8)
#     return wrap_func    

# @decorator        
# def hello(m):
#     print(m)
# @decorator            ## using the same decorator we have wrapped another function that have the same decoration ,
# def new_add(a,b):     ## or behaviour as that of 'hello()' function.
#     print(a+b)    

# hello("hiiii")    
# new_add(2,4)
##------------------------------------------------------------------------------------------------------------
##2.EXAMPLE OF PRACTICAL USAGE OF DECORATOR :- here lets make a decorator that tells about performance of another function
#                                              ex:- performance decorator,authorisation decorator , logging in decorator,etc....

# from time import time 
# def performance(func):
#     def wrapper_func(*some_args):
#         t1=time()
#         res=func(*some_args)
#         t2=time()
#         print(f"time taken :{t2-t1}s")
#     return wrapper_func
# @performance
# def tester_fuunc(n):
#     for i in range(1,n):
#         i*10 

# tester_fuunc(1000000)
##------------------------------------------------------------------------------------------------------------
##3.Another Example Of Practical Usage Of Decorartor:-  here we are creating a decorator that changes the return 
##                                                      type of the object with the desired return type 
#  
# def return_deco(func):
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper    
# @return_deco
# def return_change(m,t):
#     return m(t) 
# list1=[1,2,3]
# x=return_change(tuple,list1)
# print(type(x))
################################################################################################################



################################################################################################################
##Generators:- generators are the functions which are used to create objects , one at a time of thier needs when they are called 
#              using next() function. 

# def new_func(arwg):
#     for i in range (arwg):
#         yield i
# g=new_func(100)
# print(next(g))
# next(g)
# next(g)
# for i in g:
#     print(i)
################################################################################################################

