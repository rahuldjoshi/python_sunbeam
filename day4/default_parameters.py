# default parameters
# if you wish to allocate default arguments it must be supplied
# from right to left
# while defining the function
# otehrwise its an error

def person_details(name, address, gender="Male"):
    print(f"Name={name} & Address={address} & Gender={gender}")

person_details("Rahul Joshi","Pune")
print('*'*100)
person_details("Vibhuti Joshi","Pune","Female")