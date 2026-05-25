#Write a Python program to print all odd and even numbers from 1 to 20.
# num=0
# for i in range(1,6):
#     num+=i
# print(num)


for i in range(1,21):
    if i%2==0:
        print("number is even =",i)
    else:
        print("number is odd =",i)