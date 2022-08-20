# Scope
# global and local variable

#global variable is accessed outside and inside the function
val=500 #global variable
print(f"Outisde the function Val = {val}")

def my_function():
    print(f"Access the val inside the function {val}")

my_function()


print("#"*100)

def local_function():
    num=45 #num is called as local variable
    print(f"Value of num inside the function = {num}")

local_function()

#python is unable to find num variable outside the function
# unable to find a reference for num #error
#print(f"Accessing the value of num outside the function {num}") # error

print("#"*100)

val=50 # global variable
print(f"Accessing the value outside the function {val}")

def f_function():
    val=70 #local variable
    print(f"Access val inside the function {val}")

f_function()

# Access global variable inside local variable with global word/keyword

#to update global variable

print("#"*100)

num=50
print(f"Num Outside the function= {num}")

def gb_function():
    print("Inside my function")
    global num # it means consider num as a global variable
    num=75
    print(f"Num inside the function  {num}")

gb_function()
print(f"Num Outside the function after call=  {num}")

print("#"*100)
# Bank example

balance=5000

print(f"Initial Balance = {balance}")

def deposit():
    global balance
    balance=balance+500
    print(f"Deposit = {balance}")

def withdraw():
    global balance
    balance=balance-200
    print(f"Withdraw = {balance}")


deposit()
withdraw()
deposit()
deposit()