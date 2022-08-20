# Demo on Data types
# In python data types are inferred
# the datatypes are automatically assigned by the python
# python is dynamically typed language

# integer type of variable
num = 44
print(num)
print(type(num))  # <class 'int'>
print(f"type of num value = {type(num)}")

print()

# flaot type of value
percentage = 72.86
print(f'Percentage={percentage}')
print(f'print percentage={type(percentage)}')

print()

# string single quotes
name = 'rahul'
print(f"Name = {name}")
print(f"Type of name = {(type(name))}")  # <class 'str'>

print()
# String double quotes
sur = "joshi"
print(f"surname = {sur}")
print(f"type of sur = {type(sur)}")  # <class 'str'>

print()

# string with multi line
address="""B/5,Shreemant ganray krupa,
Patil nagar,
Balewadi,Pune - 411045"""

print(f'Address:{address}')
print(f'type of address{type(address)}')


print()

##boolean #True or False

bool=True;
print(f'value of bool:{bool}')
print(f'type of  bool:{type(bool)}')

# none
value=None
print(f'none={value}')
print(f'type of  bool:{type(value)}')
