# x="PYTHON PROGRAMMING"
# y=set(x)
# c=list(x)
# d=tuple(x)
# print("converted:",end="")
# print(c)
# print(d)
# s="100110"
# e=int(s,2)
# print("converted:",end="")
# print(e)
  
#ARITHMETIC
# a=10
# b=5
# print(a//b)

#BITIWISE OPERATOR
# a=1<<2
# print(a)

# b=a>>2
# print(b)

# c=~a
# print(c)

#SELECTION CONTROL STATEMENTS 

#IF ELSE STATEMENT 
# a=[1,2,3,4,5,6,7,8,9,0]
# x=int(input("enter you number to cheeck int the list :"))
# if x in a:
#     print(f"number {x} is present")
# else : print(f"number {x} is not present in the list ")    

#IF ELIF ELSE STATEMENTS
# d=int(input("Enter your number to check \n"))
# if d==0:
#     print("you entered the wrong number ")
# elif d%2==0:
#     print("divisible by 2")
# else :
#     print("not divisible by 2")


##CALCULATOR
# x=int(input("enter the value 1:\t "))
# y=int(input("enter the value 2:\t"))
# z=str(input("enter the operator:\t"))
# if z=='+':
#     z=x+y
# elif z=='-':
#     z=x-y 
# elif z=='*':
#     z=x*y 
# else :
#     z=x/y          
# print(f"Your Result is :\t{z}")
################################################################################################################


################################################################################################################

################################################################################################################
# x=int(input("elemets"))
# list1=[]
# for i in range(x):
#     list1.append(input(f"enter number{i} : "))
################################################################################################################
# x=int(input("no. of elements : "))
# list2=[]
# avg=0
# for i in range(x):
#     g=int(input(f"enter number {i+1} :"))
#     list2.append(g)

# for nums in list2:
#     avg=avg+nums 
# print(f"average is equal to : {avg/x}")       
################################################################################################################
# vowels=list("AEIOUaeiou")    
# my_string="Hello World"
# count=0
# for char in list(my_string):
#     if char in vowels:
#         count+=1
# print(count)        
################################################################################################################
# list1=[1,2,4,5]
# list2=[2,4,7,6]
# for nums in list2:
#     if nums in list1:
#         print(nums)
################################################################################################################

# x=10
# def plus_one():
#     global x
#     x=x+1

# plus_one()
# print(x)    


# def out_func():
#     nonlocal_var=30
#     def in_func():
#         nonlocal nonlocal_var
#         nonlocal_var=40
#         print(nonlocal_var)
#     print(nonlocal_var)
#     in_func()
# out_func()   

# def my_func():
#     print("hello")

# if __name__=='__main__':
#     my_func()    

# def isPalindrome(s: str) -> int :
#         new_list=[]
#         for i in s:
#             if(ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
#                 new_list.append(i)    
#         new_list="".join(new_list)   
#         new_list=new_list.lower() 
#         if(new_list==new_list[::-1]):
#             return True
#         return False    
# x=0
# x=isPalindrome("0P")
# print(x)

# x=int(input("enter to find factorial of: "))
# def fact(s):
#     if s==1:
#         return 1
#     else :
#         return s*fact(s-1)
# print(fact(x)) 


# m=int(input("enter to find factorial of: "))
# def facto1(s: int , x=1 ):
#     if s==1:
#         return x
#     else :
#         return facto1(s-1,s*x)
    
# print(facto1(m))   
#  
# def twoSum(nums:list[int], target: int) -> list[int]:
#         li=[]
#         for h,i in enumerate(nums):
#             if (target-i) in nums[h+1:]:
#                 li.append(h)
#                 li.append(1+nums[h+1:].index(target-i))
#         return li
# print(twoSum([2,7,11,12],9))

# print([1,2] or [1,3])
# from time import time 

# def performance(func):
#     def wrapper_func(*some_args):
#         t1=time()
#         res=func(*some_args)
#         t2=time()
#         print(f"time taken :{t2-t1}ms")
#     return wrapper_func

# # @performance
# def fact(num,res=1):

#     if num==1:
#         return res
#     else :
#         return fact(num-1,res*num)
# print(fact(5))
# @performance
# def facto(num):
#     res=1
#     for i in range(2,num+1):
#         res=res*i 
#     return res     
# # fact(5)

# print(facto(5))


###for linear regression
# from sklearn.linear_model import LinearRegression

# model = LinearRegression()
# model.fit([[1],[2],[3],[4],[5]], [35,40,50,60,65])#X parameter is on 2d bcuz there can be more than one inputs
# m = model.coef_[0]
# print(m)
# x=model.intercept_
# print(x)

###for splitting dataset for train and test
