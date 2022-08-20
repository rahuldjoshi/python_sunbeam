# user defind function
# docstring : describes about the function
# Rule : docstring must be specified immediately after you specify the
# first line of a function
def add():
    """This function is add function without any input required"""
    a = 10
    b = 5
    print(a + b)

add()  # calling function

print(f"Docstring of add function={add.__doc__}")

print("-" * 100)

def add_with_argument(x, y):
    """This function is add function with 2 argument required"""
    print(x + y)
    print(f"Docstring of add function={add_with_argument.__doc__}")

add_with_argument(1, 2) # calling function

print("-" * 100)

print(f"Docstring of print function = {print.__doc__}")

print("-" * 100)

def add_with_argument_with_return(x,y):
    """this function is add with 2 argument with return"""
    return x+y

total=add_with_argument_with_return(5,4)
print(f"add_with_argument_with_return:{total}")

def add_with_argument_with_return(x,y):
    """this function is add with 2 argument with return"""
    add_with_argument(1,2);

total_1=add_with_argument_with_return(5,2)
print(total_1);







