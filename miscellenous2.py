### FUNCTION - A FUNCTION IS BLOCK OF CODE THAT PERFORMS A SPECIFIC TASK AND CAN BE USED TO PERFORM MULTIPLE TASK ASSIGNED TO IT . IT IS WRITTEN IN THE FORM OF { def *identifer*() }.
## def dup():
##   duplicates =[]
##   some_list=['a','b','c','b','d','n','n']
##    for i in some_list :
##     if some_list.count(i)>1:
##         if i not in duplicates:
##           duplicates.append(i)
##   print(duplicates)
################################################################################################################

# def name_len(name):
#   x=len(name)
#   return print(f"your name is {x} letters long")
# def name_reverse(name):
#   x=name[::-1]
#   return print(x)
# class PlayerCharacter:
#    def __init__(self,name,age):
#      self.name=name
#      self.age=age

# player1=PlayerCharacter('Kabeer','18')
# print(player1.name)
# print(player1.age)

# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# cat1=Cat('Juju','12')
# cat2=Cat('anglo','5')
# cat3=Cat('kallu','4')




# class Employee():
#     def __init__(self,name,age,salary,department):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.department=department
#     def income(self):
#         if(self.salary>700000):
#             print("COMES UNDER TAX REGIME")
#         else :
#             print("DOES NOT COME UNDER TAX REGIME")
#         return 0
#     def age_check(self):
#         if (self.age>65):
#             print("YOUR ARE ABOUT RETIRED")
#         else :
#             print("YOU ARE NOT RETIRED")
# x=str(input("ENTER YOUR NAME: \t"))
# y=int(input("ENTER YOUR AGE:\t"))
# z=int(input("ENTER YOUR SALARY:\t"))
# a=str(input("ENTER YOUR DEPARTMENT:\t"))
# employee1=Employee(x,y,z,a)
# employee1.age_check()
# employee1.income()


# class Playercharacter(object):
#     def __init__(self,name,age,email):
#         self.email=email
#         self.age=age
#         self.name=name
# class wizard (Playercharacter):
#     def __init__(self,power):
#         self.power=int(power)
#         # print(f"you have the power of {self.power}")
#     def attack(self):
#         print(f"you have the power of {self.power}")

# class archer(Playercharacter):
#     def __init__(self,power):
#         self.power=int(power)
#         # print(f"you have {self.power} arrows left")
#     def attack(self):
#         print(f"You have attacked with {self.power} arrows")
# archer1=archer(100)
# wizard1=wizard(50)
# @staticmethod
# def attack():
#     print("done")
# for i in  [archer1.attack(),wizard1.attack()]:
#  pass

# import this


# class Employee:

#   def __init__(self, name, emp_code, emp_sal, emp_dept):
#     self.name = name
#     self.emp_code = int(emp_code)
#     self.emp_sal = emp_sal
#     self.emp_dept = emp_dept

#   def tax_check(self):
#     if self.emp_sal > 50000:
#       print(self.name, self.emp_code)


# class Department(Employee):

#   def __init__(self, work_hour, team_leader):
#     self.work_hour = work_hour
#     self.team_leader = team_leader


# class BankAccounts:
#     def __init__(self,accno,name,balance):
#         self.accno=accno
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#     def withdraw(self,amount):
#         self.balance-=amount
#     def balance_acc(self):
#         print(self.balance)   
# acc1=BankAccounts(123456,'Ram',5000)
# acc2=BankAccounts(654321,'Shyam',10000)
# acc3=BankAccounts(789012,'Mohan',15000)

# acc1.deposit(2000)
# acc2.withdraw(5000)
# acc3.deposit(3000)
# acc1.balance_acc()
# acc2.balance_acc()
# acc3.balance_acc()