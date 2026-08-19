#augmentd assignment operator 
# some_value = 5
# some_value +=3 #(used  to perform operations on varibles )
# print (some_value)
##------------------------------------------------------------------------------------------------------------
###PROGRAM NUMBER 1 - concept of complex number 
# new_axis=5+2j
# print(new_axis)
# print(type(new_axis))
# ##------------------------------------------------------------------------------------------------------------
# PROGRAM NUMBER 2 
# usrname_1 = 'super coder'
# password_1 = 'supersecret'
# print(password_1)
# long_string=''' this is a long string and is used to type in multi line strings without getting errors 
#  see its cool isn't it cool look
#  wow 
# 0   0
#   '
# -----
# '''
# print(long_string)
##------------------------------------------------------------------------------------------------------------
### PROGRAM NUMBER 3 -  to print full name using last and first name (strings concantenation)

##1.string concantenation
# first_name = 'sai'
# last_name = 'siddhi'
# full_name = first_name + ' ' + last_name 
# print(full_name) 

##2. string concantenation
# print('hello ' + 'Sai Siddhi')
##------------------------------------------------------------------------------------------------------------
### PROGRAM NUMBER 4 (Type Conversion) - we can converse one data type to another using type conversion 


## 1. Type conversion - here we know that x was an interger at fisrt but after converting its value to y as an string we can see its data type is now string 
# x=200
# y=str(x)
# print(y)
# print(type(y)) 

## 2. Type Conversion - here we can't convert a string to an interger datatype as intergers cannot store texual data but strings can hold alphabetical and numerical values  
# y = ' hi everyone'
# print(int(y))
# y="20"
# print(int(y[0]))

## 3. Type Conversion - 
# print(type(int(str(100))))
# print(type(str(100)))
##------------------------------------------------------------------------------------------------------------
### PROGRAM NUMBER 5 (Escape Sequence)

## 1. Escape Sequence - here we use back slash to tell python that whatever comes after this back slash is a part of statement in a string 
# print('it isn\'t cool')


## 2. Escape Sequence  - here we use bakslashn (\n) after an word in string to move the next word to  new line 
# print(' Hi everyone \n How are you doing')


## 3. Escape Sequnce - here we use (\t) to add a tab space between words in a strings 
# print ('Hi\t everyone\thow are you guy')
##------------------------------------------------------------------------------------------------------------
### PROGRAM NUMBER 6 (Formatted Strings) 

## 1. Formatted Strings - here we use (f) to tell python that this is a formatted string and we can use variables in it and cam assign the values parallely
# _age = 55
# _name = 'sai'
# print(f'hi everyone my name is {_name} and i\'m {_age} years old')


## 2. Formatted strings Method - here we use (.format) to tell python that here we are using a method for formatted strings and can assign the values after the string is created
# name_1 = 'sai'
# age_1 = 55
# x = 'hi everyone my name is {0} and i\'m {1} years old'
# print(x.format(name_1,age_1))

##------------------------------------------------------------------------------------------------------------
### PROGRAM NUMBER 7 (String Indexes[Start:Stop:Stepover]) 
## 1. String Indexes - here we use square brackets to tell python that we want to access a part of string and the part we want to access is stored in a identifier . 
# stng_1 = 'hi everyone'
# print(stng_1[5])

## 2. String Indxes (Limit upto index) - here after upto we use colon to tell python that upto what limit do we want to acess the idnetifier 
# spg_2 = 'Manyasurve sujal'
# print(spg_2[0:10]) 

## 3. String Indexes (Stepover Command as in Indexes) - here after upto limit we use colon and after it we give a integer through which we want to stepover with all its integral 
# stg_3 = 'it is a beautiful day'
# print(stg_3[0:20:2]) 

## 4. String Indexes (Negative Indexes or reversal) - here we use negative indexes to tell python that we want to start from the end of the identifier 
# stg_4 = 'hi everyone how are you'
# print(stg_4[::-1])
###################################################################################################################

#### BOOLEANS DATA TYPES - WE USE BOOLEANS TO MANAGE LOGIC AS TRUE OR FALSE IT CAN STORE THE VALUE AS EITHER TRUE OR FALSE 
## CONCEPT OF IMMUTAIBILITY - WE CAN'T CHANGE THE VALUE OF THE PART OF STRING AS IT IS IMMUTAIBLE THE ONLY WAY TO CHANGE THAT PART IS TO REASSIGN THE ENTIRE STRING





#######################################################################################################################
#### METHODS IN PYTHON - METHODS ARE SIMILAR TO FUNTIONS BUT THEY ARE OWNED BY SOME DATA TYPES FOR EXAMPLE STRING METHODS ARE OWNED BY STRING ONLY 

###STRING METHODS 
## 1. Uppercase Methods { .upper() } - used to captalise the whole sentence of the string 
# x = 'to be to no to be'
# print(x.upper())
##------------------------------------------------------------------------------------------------------------
## 2.Capitalize Methods { .capitalize() } - used to capitalise the first word of the sentence of the string 
# x='hi baby girl'
# print(x.capitalize())
##------------------------------------------------------------------------------------------------------------
## 3.Lowercase Methods { .lower() } - used to to lower case the whole sentence of the string 
# x = 'HI BABY GIRL'
# print(x.lower())
##------------------------------------------------------------------------------------------------------------
## 4. Find Method { .find(*to find*) } - used to find character , word , alphabet is present at starting of which index 
# x='hi baby its you who is who'
# print(x.find('who'))
##------------------------------------------------------------------------------------------------------------
## 5. Replace Method { .replace(*to replace*, to replace with*)  } - used to replace the word with the new word in a string 
# x='hi to bye is quite not a hi'
# print(x.replace('hi', 'bye'))

##------------------------------------------------------------------------------------------------------------
## 6. Split Method { .split()} - split method used to split the string into a list
# x='123456789'
# y='hello buddy how are you'
# m="1 120 123 11"
# print(m.split())
# print(y.split())
# print(x.split())
#######################################################################################################################



#######################################################################################################################
###LIST METHODS 

## 1. Append method { .append(*what to add in last*) } - used to add single new character to the list or the string at a time 
# x=['ball','bat','stumps']
# new_list = x.append('gloves')
# print(x)
# print(new_list) ###*/here we can see that append cannot create new lists but rather modifies the existing list/* 
##------------------------------------------------------------------------------------------------------------
##2. Insert Method { .insert(*index*,*what to insert*) } - used to insert new character to the list at the desirable index 
# x=[
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# new_list = x.insert(2,[100,0,2])
# print(x)
# print(new_list)
# y=[1,23,5,9]
# y.insert(3,6)
# print(y)
##------------------------------------------------------------------------------------------------------------
##3. Extend Method { .extend(*what to extend*) } - used to extend the list by multiple values at the last of the list
# x=[100,2,4]
# x.extend([9,8,1])
# print(x)
##------------------------------------------------------------------------------------------------------------
##4. Pop Method { .pop(*index at*) } - used the remove the character at the index mentioned in the method 
# x=[1,3,5,7,9,2,4,6]
# x.pop(6)       #/* here a variable can be assigned as "y=x.pop()" to store the value of the data popped from the list*/
# print(x)
##------------------------------------------------------------------------------------------------------------
##4. Remove Method { .remove(*value that is to be removed*)} -used to remove the exact value from the list mentioned in the method at whatever the index it is on 
# x=['lap','nap','map', 'gap']
# x.remove('nap')
# print(x)
##------------------------------------------------------------------------------------------------------------
##5. Clear Method { .clear() } - used to clear th entire list or like making the list empty
# x=[1,3,6,7,4,10,22]
# x.clear()
# print(x)
##------------------------------------------------------------------------------------------------------------
##6. Index Method { .index(*value to be found*,*start*,*stop*) } - used to find the index of the value mentioned in the method within the given range 
# x=['note','pen','pencil','rope','glove']
# print('rope' in x)
# y=x.index('rope')
# print(y)
##------------------------------------------------------------------------------------------------------------
##6. In Method { in } - used to check if the value mentioned in the method is present in list/string or not 
# x=['pen','note','pencil', 'rope','glove']
# y='nope'
# print('p' in y)
# print ('pen' in x)
# print('ball' in x)
##------------------------------------------------------------------------------------------------------------
##7. count method { .count(*what to be counted*) } - used to count the number of times an item is present in the list
# x=['pen','note','pencil', 'rope','glove','pen']
# y=(x.count('pen'))
# print(y)
##------------------------------------------------------------------------------------------------------------
##8. Sort Method { .sort() } - we use it to sort the list ascending
# x=[2,57,9,-2]
# b=['pen','note','pencil', 'rope','glove','pen']
# y=x.sort()
# b.sort()
# print(b)
# print(x)
##------------------------------------------------------------------------------------------------------------
##9. reverse method{ .reverse() } - used to reverse the list from its original form
# x=['amma','abba', 'appa', 'ammi']
# x.reverse()
# print(x)
##------------------------------------------------------------------------------------------------------------
##10.Join Method { .join() } - used to join the list into a string 
# x=['pen','is', 'a','good','tool']
# z=' '
# m=z.join(x)
# print(m)
##------------------------------------------------------------------------------------------------------------
##11.list unpacking { *variable name* = *list value*} - used to assign the vales of the list to the varibles 
# x,c,v, *other ,m =[1,2,3,4,5,6,7,8] 
# print(x,c,v,other,m)
##------------------------------------------------------------------------------------------------------------


#### WE ARE GONNA TALK ABOUT THE ONE OF THE MOST IMPORTANT TOPIC IN THE PROGRAMMING LANGUAGES - BUILT IN FUNCTIONS AND METHODS


## 1.Length Function { len() } -  to find lenght of a string we use len() function 
# psswrd = 'kaiflala124'
# print(len(psswrd))
##------------------------------------------------------------------------------------------------------------
## 2.Binary Functions { bin() } - to find the binary code of a number we use bin() functions 
# x = 7
# print(bin(x))
##------------------------------------------------------------------------------------------------------------
## 3.Sort Funtions { sorted() } - to sort the values in a list or strings we use sorted() functions 
# x = '16732548'
# print(sorted(x))
#######################################################################################################################





###########################################################################################################

### DICTIONARY { keyword - dict } - it is a advance form of list or tyoe of data structure used to store different types of data in a single shell or various shell it deals with complex data .

### METHODS FOR DICTIONARIES - methods in dictionary are used to access the data stored in it and to perform different operations.one can create a dictionary using ( dict ) keyword 
##                             variable={*key*:*values*}
# user2= dict(name='sai',age=55)
# print(type(user2))
# user2['age']=int(user2['age'])+10
# user2['date']='12/12/12'
# print(user2)
##-----------------------------------------------------------------------------------------------------------
## 1. get method { .get(*key*,*values*) } - used to get the value stored in particalar key of dictionary . it also helps in dealing wth errors if the key is not found in the dictionary and the value assigned in get method will be used as final value . this function doesn't modify the dicionary but rather customizes it temporarily  .//##note here the value will be updated if the is already present in the directionary 
# user = {'abbu': [1, 3, 5, 7], 'alli': 'hi', 'age': 20}
# print(user.get('roll call', 243132))
# print(user)
##-----------------------------------------------------------------------------------------------------------
## 2. In Method { in } - used to check if the item/key in case of dictionary mentioned in the method is present in list/string/dictionary or not 
# user1= dict(name="sai",age="15")
# x='sai' in user1
# print(x)
##-----------------------------------------------------------------------------------------------------------
## 3. Key methods { .key() } - used to check if the key is present in the dictionary or not
# user = {'abbu': [1, 3, 5, 7], 'alli': 'hi', 'age': 20}
# print('abbu' in user.keys())
##-----------------------------------------------------------------------------------------------------------
## 4. values methods { .values() } - used to check if the value asked is present in dictionary or not 
# user = {'abbu': [1, 3, 5, 7], 'alli': 'hi', 'age': 20}
# print('hi' in user.values())
##------------------------------------------------------------------------------------------------------------
## 5. Items methods { .items() } - used to access the whole item as in key as well as the value 
# user = {'abbu': [1, 3, 5, 7], 'alli': 'hi', 'age': 20}
# print(user.items())
##------------------------------------------------------------------------------------------------------------
## 6. Clear method { .clear() } - used to clear the whole dictionary 
# user = {'abbu': [1, 3, 5, 7], 'alli': 'hi', 'age': 20}
# user.clear()
# print(user)
##------------------------------------------------------------------------------------------------------------
## 7. Copy method { .copy() } - used to copy the whole dictionary 
# user = {'abbu': [1, 3, 5, 7], 'alli': 'hi', 'age': 20}
# m=user.copy()
# print(m)
##-------------------------------------------------------------------------------------------------------------
## 8. pop method { .pop() } - used to pop out the value out of the dictionary 
# user = {'abbu': [1, 3, 5, 7], 'alli': 'hi', 'age': 20}
# m=user.pop('abbu')
# print(m)
# print(user)
##-------------------------------------------------------------------------------------------------------------
## 9.Popitem method { .popitem() } - used to pop out the last item of the dictionary 
# user = {'abbu': [1, 3, 5, 7], 'alli': 'hi', 'age': 20}
# m=user.popitem()
# print(m)
# print(user)
##-------------------------------------------------------------------------------------------------------------
## 10.Update method { .update(*key*:*new value to key*) } - used to update the value stored in the key of the dictionary 
# user = {'abbu': [1, 3, 5, 7], 'alli': 'hi', 'age': 20}
# user.update({'age':40})
# print(user)
##-------------------------------------------------------------------------------------------------------------
## 11.Setdefault method { .setdefault(*key*,*value*) } - used to set the value of the key in the dictionary if the key is not present in the dictionary .
# user = {'abbu': [1, 3, 5, 7], 'alli': 'hi', 'age': 20}
# user.setdefault('age',40)
# print(user)
##______________________________________________________________________________________________________________

##############################################################################################################





###############################################################################################################

### TUPLES - TUPLES ARE LIKE LIST BUT RATHER IMMUTABLE THAT IS THEY CANNOT BE CHANGED FROM ITS INTIAL FORM .(TUPLE IS IMMUTABLE) MOST FUCNTION OR METHOD CANNOT BE USED TO OPERATE IT . IT IS WRITTEN IN PARENTHESES ().UNPACKING OF THE TUPLE IS POSSIBLE THO.
# y,x,*z=(1,2,3,4,5)
# print(z,x,y)
# #OR 
# my_tuple=(1,2,4,5,6)
# m=my_tuple[0]
# b=my_tuple[1]
# print(m,b)
# print(my_tuple[0:3])

##METHODS AND FUNCTIONS THAT CAN BE USED IN TUPLES ;
##1. count method
##2. Length function
##3. Index Method
##4. In method
##5. Sorted Funtion
##6. Max function
##7. Min function 
#######################################################################################################################






#############################################################################################################
####NOTE- 'is' operator is used to compare adress of two opernads where as '=='is used to compare the value 
##         of the two operand
#############################################################################################################



#######################################################################################################################
### SETS - SETS ARE ALSO AS SAME AS LIST AND TUPLES BUT THEY AE UNORDERED COLLECTION OF UNIQUE OBJECTS . THEY ARE  WRITTEN WITHIN THE CURLY BRACES {} AND ARE NON-CHANGEABLE BUT WE CAN ADD NEW OBJECTS TO IT . 

##METHODS THAT WORKS IN SETS  - 
##1.ADD METHOD
##2.REMOVE METHOD
##3.DISCARD METHOD 
##4. POP METHOD
##5. CLEAR METHOD 
##6. DELETE KEYWORD 
##7. COPY METHOD 
##9. CLEAR METHOD
#######################################################################################################################






#######################################################################################################################
##SPECIAL FUNCTIONS IN PYHTON :-

##------------------------------------------------------------------------------------------------------------
##1.Map Function:-  used for mapping of any iterable provided according to the given function { map(<function>,<iterable>) }
# def if_even(a):
#     return a%2==0
# my_buck=[20,3,5,22,4]
# var=list(map(if_even,my_buck)) #in place of normal function lambda function can also be used 
# print(var)
##------------------------------------------------------------------------------------------------------------
##2.Lambda Function :- also knowns as one-line function or nameless function { lambda <variable>: <expression_on_var> }
# x=[1,3,5]
# var_1=list(map(lambda a : a*a,x))
# print(var_1) 
##------------------------------------------------------------------------------------------------------------
##3.Filter Function :-used for filteration of desired value from the iterable { filter(<function>,<iterable>) }
# def if_even(a):
#     return a%2==0
# y=[3,4,7,9,10,14,2]
# var_2=list(filter(if_even,y)) ##samething can be done using map func  but we can observe that map function just maps the returned value not the actual data from iterable
# print(var_2)
##------------------------------------------------------------------------------------------------------------
##4.Zip function :- used to zip two iterables together { zip(<iterable1>,<iterable2>) }
# list1=[-1,3,-5]
# list2=[-200,41,60]
# list3=list(zip(list1,list2))
# print(f"list3 is:{list3}")
# list3.sort(key=lambda x:x[1])##sorts the list based on the second element of the list
# print(list3)
##------------------------------------------------------------------------------------------------------------
##5.Reduce Function :- used to reduce the iterable into single value according to the given function
# from functools import reduce
# list4=[1,2,3,4]
# def accumulator(acc,item): #this function is an accumulator 
#     return acc+item
# print(reduce(accumulator,list4,0)) #here the zero is inital value of acc 
#######################################################################################################################








#######################################################################################################################
##LIST,DICTIONARY,SET COMPREHENSION :

##------------------------------------------------------------------------------------------------------------
##1.List Comprehension :-( list_name=[ <expression> for <var_name> in <iterable> if <condition> ] )

# my_list=[char for char in "hello"] #it is shorter version of creating list from iterable
# print(my_list)
# my_list2=[nums*2 for nums in range(1,30) ]
# print(my_list2)
# my_list3=[nums**2 for nums in range(1,21) if nums%2==0]
# print(my_list3)

##------------------------------------------------------------------------------------------------------------
##2.Set Comprehension :- { set_name={<expression> for <var_name> in <iterable> if <condition>} }

# my_set={nums*2 for nums in range(1,11)}
# new_set={item*2 for item in my_set}#new_set will always contain the same values as of my_set as sets are immutable after their creation
# print(my_set)
# print(new_set)

##------------------------------------------------------------------------------------------------------------
##3.Dictionary Comprehension :- { dict_name={<expression> for <var_name> in <iterable> if <condition>}

# my_dict={
#     'a':2,
#     'b':3,
#     'c':5
# }
# new_dict={ key:value**2 for key,value in my_dict.items()}
# print(new_dict)
##------------------------------------------------------------------------------------------------------------
#######################################################################################################################


