# waf to check number pass by argument is odd or even


# def check_number(n):
#     if n%2 ==0:
#         print (f"{n} is an even number.")
#     else:
#         print (f"{n} is an odd number.")
# check_number(int(input("Enter a number: ")))

 
#waf to check which number is greater and two number by user
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
def check_greater(a,b):
    if a > b:
        print(a,"is greater than",b)
    elif b > a:
        print(b,"is greater than",a)
    else:
        print("Both numbers are equal.")        
check_greater(5,10)


#waf to check the number is vowels are consonats

# def check_vowel_consonant(char):
#     vowels = 'aeiouAEIOU'
#     if char in vowels:
#         print(char,"is a vowel.")
#     elif char.isalpha():
#         print(char,"is a consonant.")
#     else:
#         print("Invalid input. Please enter a single alphabetic character.")

# check_vowel_consonant("b")

#waf to check the number is divisible by 2 and 3 and return
#" yes number is completely divisible by 2 and 3"
#" no number is not completely divisible by 2 and 3"
# def check_divide(n):
#     if n%2==0 and n%3==0:
#         print("Yes, number is completely divisible by 2 and 3.")
#     else:
#         print("No, number is not completely divisible by 2 and 3.")
        
# check_divide(12)

def len_of_string(s):
    c=0
    for i in s:
        c+=1
    return c
res=len_of_string("python")
print(res)