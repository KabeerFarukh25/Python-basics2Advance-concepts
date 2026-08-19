##CONCEPT OF A)GLOBAL & LOCAL ATTRIBUTES ,B)STATIC AND CLASS METHODS

# class Player():
#     membership=True #Global Attribute of Class Player
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age    #local attributes/properties instantiated inside constructor 
#         self.profile='random'
#     @classmethod #this is used to create methods that accessable by objects as well as thier classes
#     def add_two(cls,a,b):  #here cls is representing the class of its scope 
#         return a+b 
#     @staticmethod
#     def add_two_2(a,b):#here cls is not required as the programmer has no command over its scope 
#         return a+b
    
# player1=Player('kabeer',17)
# print(player1.name)
# print(player1.age)
# print(player1.profile)
# print(Player.add_two(3,4))#acesssing method of any class directly without instantiating the object
# print(player1.add_two_2(1,8))#accessing method(declared using static method) of class using object 
# print(player1.add_two(1,2))#accessing method(declared using class method) of class using object 

##########################################################################################################
 
##CONCEPT OF PRIVATE ATTRIBUTES IN PYTHON :- 
# python itself does not have any feature of private or public .Hence to declare private variable we use underscore before identifier
#it it not a strict rule but a convention set by programmers to indicate that it is private variable 
  
# class PlayerCharacter():
#     def __init__(self,name,age):
#         self._name=name#declaration of private variable 
#         self._age=age

#     def get_age(self):
#         return self._age    
# player1=PlayerCharacter('Kabeer',18)
# print(player1._age) 
# player1._name='kabbu'
# print(player1.get_age())#this will print the value of private variable _age of player1
# print(player1.get_age)#this will print the memory address of the function

#############################################################################################################################################################################

##INHERITANCE OF LOCAL ATTRIBUTES IN PYTHON :- Subclass can only access the attributes of its parents class if they are declared as global attributes 
##                                             if they are declared inside any method of parent class then they are need to be passed to the child class explicitly
##                                             using super() function or using the name of the parent class .



# class Employee(object):
#     def __init__(self,emp_id):
#         self.emp_id=emp_id
# class Manager(Employee):
#     def __init__(self,name,age,emp_id=0):#here emp_id is default parameter of value 0
#         super().__init__(emp_id)#this will call the constructor of parent class and pass the value of emp_id to it
#         self.name=name
#         self.age=age
# class HR(Employee):
#     def __init__(self,name,age,emp_id=0):#here emp_id is default parameter of value 0
#         Employee.__init__(self,emp_id)#this will call the constructor of parent class and pass the value of emp_id to it
#         self.name=name
#         self.age=age

# employee1=Manager('Ramu',28)
# employee2=Manager('Kabeer',18,'E001')
# employee3=HR('Kabbu',17,'E002')
# print(employee1.emp_id)
# print(employee2.emp_id)
# print(employee3.emp_id)
# del employee1#this will delete the object employee1 and its attributes

# ## INTROSPECTION : this list out all the attrbutes and methods available for the object
# print(dir(employee2))


##USAGE OF OBJECTS IN CLASSES :- every built-in function in python is built using the dunder methods or magic methods, hence every built-in function used in python is an object

# class A(list):
#     def __init__(self,a):
#         return self.append(a)
    
# c=A(5)#Here you can see that we are using class A as a list and appending the values to it
# c.append(2,3) 
# c.append(3)   
# c.append(12) 
# print(c)
# l=[1,23,4]
# print(l)
# class B():
#     def __str__(self):
#         return self.__str__
# x=B()    
# print(x.__str__())

##__str__ is used to return the string representation of the object 
   
####################################################################################################################################

### DUNDER METHODS or MAGIC METHODS :- Dunder methods are the methods that works under the hood and are used to 
##  implement the built-in funtions in python generally they are not to be overridden but for some edge cases
##  we can override them according to our need 

# class A(list):
#     def __init__(self,a):
#         self.a=a
#     def __append__(self):
#         return super().extend(iter)
#     def __str__(self):
#         return 'this is a list' 

# c=A(5)
# c.append(2)
# l=[1,3,4,5]
# l.append(2)
# print(l)
# print(c)
# c.extend(l)
# print(c)
# l
# print(l)
# print(c)



