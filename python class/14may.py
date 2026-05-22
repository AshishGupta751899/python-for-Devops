# wap to count the space in the given string : "this is python"
var1="this is python"
count=0 
for i in var1:
    if i==" ":
        count+=1
print("Number of spaces:", count)

# var1="this is python"
# count=0 
# for i in var1:
#     if i !=" o":
#         count+=i
# print("string after eliminating 'o':", count

# wap to count the number of digits in the given string : "address="D-1 267/268 MAYUR-VIHAR-PHASE3 110096"

# var1="D-1 267/268 MAYUR-VIHAR-PHASE3 110096"
# count=0
# for i in var1:
#     if i.isdigit():
#         count+=1    
# print("Number of digits:", count)

# var1="D-1 267/268 MAYUR-VIHAR-PHASE3 110096"
# c=0
# number="1234567890"
# for i in var1:
#     if i in number:
#         c+=1
# print(c)
        

        #while loop 
          # initializer 
          # condition
          # increment/decrement


# wap to print only even numbers from 10 to 20 using while loop
 
start=10
end=20
while start<=end:
    if start%2==0:
        print(start)
    start+=1
