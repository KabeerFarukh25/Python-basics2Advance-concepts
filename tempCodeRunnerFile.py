# class Vehicle:
#     def __init__(self):
#         self.__vehicle_id=None
#         self.__vehicle_cost=0
#         self.__vehicle_type=None
#         self.__premium_amount=0
#     def set_vehicle_id(self,id):
#         self.__vehicle_id=id    
#     def get_vehicle_id(self):
#         return self.__vehicle_id
#     def set_vehicle_cost(self,cost):
#         self.__vehicle_cost=cost   
#     def get_vehicle_cost(self):
#         return self.__vehicle_cost    
#     def set_vehicle_type(self,type):
#         if type=="Two Wheeler" or type=="Four Wheeler":
#             self.__vehicle_type=type
#         else :
#             print("Invalid Vehicle Type")    
#     def get_vehicle_type(self):
#         return self.__vehicle_type
#     def set_premium_amount(self,amount):
#         self.__premium_amount=amount
#     def get_premium_amount(self):
#         return self.__premium_amount
#     def calculate_premium(self):
#         if(self.get_vehicle_type()=='Two Wheeler'):
#             if self.get_vehicle_cost()==None:
#                 print("Set Vehicle Cost First")
#             else:    
#                 self.set_premium_amount(self.get_vehicle_cost() * 0.02)
#         elif self.get_vehicle_type()=='Four Wheeler':
#             if self.get_vehicle_cost()==None:
#                 print("Set Vehicle Cost First")
#             else:    
#                 self.set_premium_amount(self.get_vehicle_cost() * 0.06)        
#     def vehicle_details(self):
#         print("Vehicle Id ",self.get_vehicle_id())
#         print("Vehicle Cost ", self.get_vehicle_cost())      
#         print("Vehicle Type ", self.get_vehicle_type())
#         print("Vehicle Premium ", self.get_premium_amount())

# vehicle1=Vehicle()
# vehicle1.set_vehicle_cost(150000)
# vehicle1.set_vehicle_id(24132425)
# vehicle1.set_vehicle_type("Four Wheeler")
# vehicle1.calculate_premium()
# vehicle1.vehicle_details()




# class Student:
#     def __init__(self):
#         self.__std_id=0
#         self.__age=0
#         self.__marks=0
#     def set_std_id(self,id):
#         self.__std_id=id
#     def get_std_id(self):
#         return self.__std_id
#     def set_age(self,age):
#         self.__age=age
#     def get_age(self):
#         return self.__age
#     def set_marks(self,marks):
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
#     def age_validate(self):
#         if self.get_age()>20:
#             return True
#         else :
#             return False
#     def marks_validate(self):
#         if self.get_marks()>=0 and self.get_marks()<=100:
#             return True
#         else :
#             return False 
#     def check_qualification(self):
#         if self.marks_validate() and self.age_validate() :
#             if self.get_marks()>=65 :
#                 return True
#             else :
#                 return False
#         else:
#             return False    



# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# import matplotlib.pyplot as plt 
# import pandas as pd 
# import numpy as np

# data=pd.read_csv("/Users/kabeerfarukh25/Desktop/Programming/Dataset/ChurnData.csv")
# print(data)



