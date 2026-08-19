# import os 
# f1=open("/Users/kabeerfarukh25/Programming/PyhtonBasics/FileHandlingtest.txt",'r')
# print(f1.read())
# print("mode: ",f1.mode)
# print("file name: ",f1.name)
# print("is file closed? ",f1.closed)
# f1.close()
# print("is file closed? ",f1.closed)

# with open("/Users/kabeerfarukh25/Programming/PyhtonBasics/FileHandlingtest.txt",'w') as file:
#     file.write("hello python\n")
#     file.write("new line written")
#     # print(file.read())

# with open("/Users/kabeerfarukh25/Programming/PyhtonBasics/FileHandlingtest.txt",'r') as file:
#     print(file.read())



# write a python program to copy its content from one file to another
# f1=open("/Users/kabeerfarukh25/Programming/PyhtonBasics/FileHandlingtest.txt",'r')
# f2=open("/Users/kabeerfarukh25/Programming/PyhtonBasics/Filecopy.txt",'w')
# f2.write(f"{f1.read().capitalize()}")


# file=open("/Users/kabeerfarukh25/Programming/PyhtonBasics/FileHandlingtest.txt",'a')
# file.write("\nThis is new line appended through apended mode")

# print(os.path.exists("/Users/kabeerfarukh25/Programming/PyhtonBasics/FileHandlingtest.txt"))

# f1=open("/Users/kabeerfarukh25/Programming/input&result.txt",'w')
# inp1=int(input('ENTER FIRST VALUE: '))
# inp2=int(input("ENTER THE SECOND VALUE: "))
# f1.write(f"input 1:- {inp1}\ninput 2:- {inp2}\nres:- {inp1+inp2}\n")
# f1.close()