# what is function?
# every function has their own purpose.
# function which executeion(code) which execute inside its owwn block.
# function is resable means define one time use many time(DRY - Don't Repeat Yourself).
# Function has two main parts first function defination second function calling 
# This is Delta 

# FUNCTION DIVIDES INTO FOUR CATEGORIES
# Take nothing and return nothing
# take nothing and return something
# take something and return nothing
# take something and return something

# Parameters and arguments
def add(a=0,b=0):
     print(a+b)
     
add(11,22)


def table_print(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
m=2
table_print(m)

