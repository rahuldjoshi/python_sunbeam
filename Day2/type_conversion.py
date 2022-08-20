# type conversion
# the process to convert one variable from one datatype to another datatype
# implecit type conversion
num=10
f_val=5.5
print(f'num={num} Type={type(num)}')
print(f'f_val={f_val} Type={type(f_val)}')

total=num+f_val
print(f'total={total} Type={type(total)}')

num=f_val
print(f'after update num={num} Type={type(num)}')
print(f'f_val={f_val} Type={type(f_val)}')
total=num+f_val
print(f'total={total} Type={type(total)}')



num=55
string="hello"
print(f'num={num} Type={type(num)}')
print(f'str={string} Type={type(string)}')
#total_exp=num+str
#print(f'total_exp={total_exp} Type={type(total_exp)}')



# num was inially was of type 'int'
# str(num) it will be considered as String by python
# conversion from int to str by using builtin function str()
# EXPLICIT CONVERSION

num=25
my_str="Python"
print(f"Num = {num} Type = {type(num)}")
print(f"str = {my_str} Type = {type(my_str)}")

addition=str(num)+my_str  #str(num) it converts int to str
   #   "25" + "Python"
   # + is used for concatination(joining) of strings
print(f"Addition = {addition} Type = {type(addition)}")



n1=4
f1=5.5
res=n1+f1
print(f"res = {res} type = {type(res)}")

print(f"res = {res} type = {type((int)(res))}") #explicit type conversion