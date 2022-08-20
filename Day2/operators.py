# we use operators in expression
# expression is a statement, which may have atleast one operator
# {} ===> string interpolation
# you can use string interpolation while writing the statement
# print("") ==> not an expression ==> it is just statement
# print(f"____{}")==> {} expression will be evaluated

# arithmetic operator
num1=25
num2=15
print(f'num1={num1}   num2={num2}')
print(f"Num1 + Num2 = {num1+num2}")
print(f"Num1 - Num2 = {num1-num2}")
print(f"Num1 * Num2 = {num1*num2}")
print(f"Num1 / Num2 = {num1/num2}")
print(f"Num1 % Num2 = {num1%num2}")
print(f"Num1 // Num2 = {num1//num2}")
print(f"Num1 ** Num2 = {num1**num2}")

#repetation
print(f"'hello is printed 5 times={'hello '*5}")
print("-"*75)

# comparasion operator
print(f"{num1} > {num2} = {num1>num2}")
print(f"{num1} >= {num2} = {num1>=num2}")
print(f"{num1} < {num2} = {num1<num2}")
print(f"{num1} <= {num2} = {num1<=num2}")
print(f"{num1} != {num2} = {num1!=num2}")
print(f"{num1} == {num2} = {num1==num2}")


print("-"*80)
#comparing strings

str1='python'
str2='java'
str3='python'
str4='Python'

print(f"{str1} == {str2}  {str1==str2}")
print(f"{str1} == {str3}  {str1==str3}")

print("-"*80)

# logical operator

v1=True
v2=False
print(f"{v1} and {v2}  = {v1 and v2}")
print(f"{v1} or {v2}  = {v1 or v2}")
print(f"not {v2} = {not v2} ")

print("-"*80)

# assignment operator

# += / -=  / *=  /  /=  / %=  Shorthand operators
my_val=50
my_val+=5;  #my_val = my_val+5
print(my_val)
my_val*=5 # my_val = my_val*5
print(my_val)

