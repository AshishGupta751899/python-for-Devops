# # traversing a string using range
# name ="python"
# size=len(name)
# for i in range(size):
#   print(name[i],end="") #end is used to print in the same line


# #without using range
# name ="python"
# for i in name:
#     print(i) #end is used to print in the same line


# var1="devops engineer"
# for i in var1:
#     if i=="e":
#     print(i,end="") #end is used to print in the same line


    # wap to count all the vowels from the given string : "this is devops batch",

# var1="this is devops batch"
# vowels="aeiouAEIOU"
# count=0
# for i in var1:
#     if i in vowels:
#         count+=1
# print("Number of vowels:", count)

#wap to print yourname in reverse order  
#   
name="Ashish"
rev=""
for i in name:
    rev= i+rev
print(rev, end="")
