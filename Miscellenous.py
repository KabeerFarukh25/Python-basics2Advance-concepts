###############################################################################################################################

# #(NOTE-DIFFERENCE BETWEEN REFERENCE VARIABLE AND POINTER VARIABLE ):-
#   a.  pointer variable is wild and can be used to traverse various memory locations using pointer arithematics and only pointers can 
#       access the dynamically allocated memory
#   b.  reference variables is bounded to one variable only and can be used to traverse the memory of the variable it is bounded with ,
#       dynamic memory cannot be accessed by the reference variables
################################################################################################################################



###############################################################################################################################
##THIS IS A GREAT EXAMPLE OF REFERENCES IN PYTHON

##SHALLOW COPY (Means - A new variable is created and it stores the value of original item)
##(NOTE - Any change in the value of shallow copy object will not be reflected on original object,
#         A shallow copy creates a new object, but does not copy nested objects—changes to nested 
#         objects affect both copies.)

##EXAMPLE 1.
# m=[1,3,2,4]
# g=m.copy()     ##Shallow copy
# g.append(5)
# print(m)
# print(g)
# print(g==m)
# print( g is m)

##EXAMPLE 2.
# import copy
# original = [1, 2, [3, 4]]
# shallow = copy.copy(original)
# shallow[0] = 99           # Only changes shallow copy
# shallow[2][0] = 88        # Changes both shallow and original (nested list)
# print("Original:", original)  # Output: [1, 2, [88, 4]]
# print("Shallow:", shallow)    # Output: [99, 2, [88, 4]]



##-------------------------------------------------------------------------------------------------------------------------------
##DEEP COPY (Means - A new variable created is pointing/reffering to the original variable or item )
##(NOTE - any change in the value of deep copy object will be reflected on the original object or value.
#         A deep copy creates a new object and recursively copies all nested objects—changes to nested
#         objects do not affect the original.)

##EXAMPLE 1.
#m=[1,3,2,4]
#g=m          ##Deep Copy
#g.append(5)
#print(m)
#print(g)
#print(g==m)
#print( g is m)

##EXAMPLE 2.
# import copy
# original = [1, 2, [3, 4]]
# deep = copy.deepcopy(original)
# deep[0] = 99              # Only changes deep copy
# deep[2][0] = 88           # Only changes deep copy (nested list)
# print("Original:", original)  # Output: [1, 2, [3, 4]]
# print("Deep:", deep)          # Output: [99, 2, [88, 4]]
################################################################################################################################



################################################################################################################################
###(NOTE- FUNCTION PARAMETERS :- there are various ways a parameter can be passed to a functions . EG:-) 
##-------------------------------------------------------------------------------------------------------------------------------
##1.POSITIONAL ARGUMENT PASSING:-while passing arguments simply , order of arguments must be in proper sequence
##2.KEYWORD ARGUMENT PAASING:- it is generallly a bad convention to pass the arguments using keywords explicity , but can be done if necessary

# def greet(name="Anonymous",emoji=":<)"):
#     print(f"Hey {name}!!! {emoji}")
# greet("Kamir",":)")                   ##example positional argument passing 
# greet(":)","Zain")                    ##example setback of positional argument passing 
# greet(emoji=":|",name="Momu")         ##example keyword argument passing 
# greet(emoji=":-(",name="Chomu")       ##advantage keyword argument passing 
# greet()
##3.DEFAULT ARGUMENT PASSING:-while creating a function we usually give default arguments, which works as a default parameter even if no arguments were given while calling the function.

##-------------------------------------------------------------------------------------------------------------------------------
################################################################################################################################



################################################################################################################################
##(NOTE- "is" operator is used to compare the memory address of variables or objects )
################################################################################################################################



################################################################################################################################
## (NOTE- FUNCTION AS VARIABLES :- In python functions are also variables or identifiers that can be referenced and passed to any other function)

##------------------------------------------------------------------------------------------------------------
# def hello():
#     print("hello")
# greet=hello## here the variable is used to reference to one function
# greet() ## variable of function is called explicitly 
# del hello
# greet()
# a important point to remember is even after the deletion of parent function the reference function will still point to the same function and 
# will behave same way
# greet()        
##------------------------------------------------------------------------------------------------------------
# def call(func):
#     func()
# def hello():
#     print("helllloooo")
# a=call(hello)
# print(a)
################################################################################################################################



################################################################################################################
## FUNCTIONS CACHING :- it is way or functionality of python programmming to enable the functions to run faster
##                      after their first execution if called with same input as their first call . it works by 
##                      saving the call values of the first execution and saving it in cache memory.
################################################################################################################
##CORRECT WAY OF FUNCTION CACHING:-here we will be returning the values from cache function that will be stored in 
##                                 cache memory and can be used for faster function execution if called with same 
##                                 arguments and will not be dependent on its side effects.
# from functools import lru_cache
# import time
# @lru_cache
# def factorial(a):
#     fact=1
#     for i in range(1,a+1):
#         fact=fact*i
#     time.sleep(5)    
#     return fact    
# print(factorial(10))
# print("first time done")
# print(factorial(10))
################################################################################################################
##THIS IS A WRONG WAY OF FUNCTION CACHING :- This is a wrong way of function caching as function caching saves the
##                                           returned values from function and not its side effects .
# from functools import lru_cache
# import time
# @lru_cache
# def some_function(x):
#     for i in range(x):
#         print(f"executing for {i+1} times") #side affect 
#         time.sleep(2)


# some_function(5)
# print("done for 1st time")
# some_function(5)
################################################################################################################



################################################################################################################################
##(NOTE- CONCEPT OF PURE FUCTION ):-
##        a.Pure functions are functions which does not affect the real world (by real world it is meant the input/output devices)
##        b.Pure Functions always give unique values for same inputs.
################################################################################################################################



################################################################################################################################
##(NOTE - WAY TO ANNOTATE/HARDCODE THE RETURN TYPE OF A FUNCTION ):-
##                      TO HARDCODE THE RETURN TYPE OF A FUNCTON WE USE ARROW OPERATOR TO ANNOTATE THE RETURN TYPE
##                      OF THE FUNCTION.

##1.EXAMPLE:-
# def ascii(x) -> int:
#     return ord(x)
# print(ascii('a'))

##2.EXAMPLE:-
# def list_breaker(x)->list:
#     return x[0:int(len(x)/2)]
# k=[1,2,3,4,4]
# print(list_breaker(k))
################################################################################################################################

################################################################################################################################
##(NOTE - WAY TO HARDCODE THE DATATYPE OF PARAMETERS OF FUNCTION):-

##1.EXAMPLE:-
# def plus_five(m:int)->int:
#     return m+5
# print(plus_five(10))

##2.EXAMPLE:-
# def list_sqr(x:list)->list:
#     return [i*i for i in x]
# li=[1,2,3,4]
# print(list_sqr(li))

################################################################################################################################




################################################################################################################################
##(NOTE - CONCEPT OF HIGHER ORDER FUNCTION HOC ):-
##           a.they are the function which can either acccept function as parameters or which can return functions 
##           b.Example :- map(),filter(),reduce(),etc
##-------------------------------------------------------------------------------------------------------------------------------
##1.
# def hello(greet):
#     greet()
##-------------------------------------------------------------------------------------------------------------------------------
##2.
# def main_func(x):
#     return x()
################################################################################################################################





################################################################################################################################
## OBJECT INTERNING :-
##                      1) object interning is a memory optimisation method used to improve performance and reduce memory usage in pyhton.
##                      in python if two immutable items are created and both holds the same value then rather than creating a new memory 
##                      cell for each item python creates only one memory cell for both the items.
##                      2) If there is any request in change of value of any one variable then the different memory cell be assigned to each
##                      variables.  
##                      3)Python applies interning only to immutable objects, such as:
##                          a.Small integers (typically -5 to 256).
##                          b.Strings that are short and consist of alphanumeric characters.
##                      4)scope of interning:-
##                          a.Small integers and some strings are automatically interned by Python.
##                          b.Larger integers and more complex strings may not be interned unless explicitly requested.
##                      5)This is one of the advance techinque to improve the memory efficiency in python 

# x=int(10000000000000000)
# y=int(10000000000000000)
# print(x is y)
# print(id(x))
# print(id(y))
# print(type(x))
######################################################################################################################



######################################################################################################################
### ERROR HANDLING IN THE PYTHON :
##the keyword 'raise' is used in line to raise the error when condition is not reached 

##-------------------------------------------------------------------------------------------------------------------------------
##EXAMPLE 1.

# def natural_num(n):
#   if n<0 or n>9: 
#     raise ValueError(f"The number {n} is not the natural number.Input the value between the range 0 to 9 ") 
#   return (n) 

# try:              #try command tries to code and terminates when an error is found or raised,it does not raises error but rather run the except block 
#   for i in range(0,15):
#     print(natural_num(i)) 

# except ValueError as e:         #except command block runs the code only when an error is raised in the try command block
#   print(e)

# finally:         #finally command block will always run the code irrespective of whether the error is raised or not by except and try block
#   print("IMPORTANT LINE OF CODE")

##-------------------------------------------------------------------------------------------------------------------------------
##EXAMPLE 2.

# class InvalidAgeError(Exception):
#     print("Invalid age.Invalid age error occured")

# def check_age(age):
#     if age<0:
#         raise InvalidAgeError

# try :
#     check_age(-12) 
# except InvalidAgeError as e:
#     print(e)         

################################################################################################################



################################################################################################################

# REGULAR EXPRESSIONS:

# import re
# pattern=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!#%*?&]{8,18}$")
# strings='ab?=AM#AMA@'
# a=pattern.search(strings)
# print(a)
# password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
# re.match(password_pattern, 'secret')# Returns None
# m=re.match(password_pattern, '-Secr3t.') # Returns Match object
# print(m.string)

################################################################################################################



################################################################################################################
##CREATE A GENERAL TYPE FUNCTION THAT COULD ACCEPT BOTH LIST AND STRING
# from typing import Sequence, TypeVar
# U = TypeVar('U')
# def list_str_breaker(x: Sequence[U]) -> Sequence[U]:
#     mid = len(x) // 2
#     return x[:mid] #Function to accept both strings and lists and return the same type, use a generic Sequence TypeVar as shown.

# string="some string written"
# list1=[1,2,3,4,5,6]
# print(list_str_breaker(list1))
# print(list_str_breaker(string)) 

################################################################################################################



################################################################################################################
##TRAILING COMMA RULE :- the trailing comma in a list,set,disctionary and tuples are preffered because it 
#                           1.Reduce syntax errors
#                           2.Make code easier to modify
#                           3.Keep diffs clean
#                           4.Improve readability
#                           5.Support multi-line formatting
##examples:-
# list1 = [1, 2, 3, 4]#novice way of convention
# list2 = [1, 2, 3, 4,]# good writing convention
#****NOTE:- a tuple with only one element must be seperated out with trailing comma 
# x=('hello')#->string
# y=('heelo',)#->tuple
 


################################################################################################################