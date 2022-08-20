#function with parameters and no return value
#positional Parameters

def print_emp_info(name,age,id,dept):
    print(f"Name = {name}")
    print(f"Age = {age}")
    print(f"ID = {id}")
    print(f"Dept = {dept}")

print_emp_info("Akshita",35,123,"training")

print("-"*100)
print_emp_info(name="person1",age=25,id=456,dept="admin")