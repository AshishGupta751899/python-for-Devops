#slicing
# marks=[10,20,30,40,50,60,70,80]
# # [start-0:stop-1:step-1]

# sub_list=marks[0:8:2]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80]
# sub_list=marks[0:8:3]
# print(sub_list)

# #reverse list
# marks=[10,20,30,40,50,60,70,80]
# sub_list=marks[0::-1]
# print(sub_list)

# #6.Traversing
# marks=[10,20,30,40,50,60,70,80]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#         print(f"this number is even : {marks[i]}")
#     else:
#         print(f"this number is odd : {marks[i]}")



# marks=[10,20,30,40,50,60,70,80]
# total=0
# for i in marks:
#     total=total+i
# print(total)
        
# marks=[10,11,20,30,40,50,60,70,80]
# sub_list=marks[2:-1]
# print(sub_list)

# wap to swap the first value of list with last value of list
# marks=[10,11,20,30,40,50,60,70,80]
# a=marks[0]
# marks[0]=marks[8]
# marks[8]=a
# print(marks)

# wap to find the sum of the all elements in the list : [10,20,30,40] 

# list=[10,20,30,40]
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)

#wap to find the sum of only even elements in the list : [10,3,4,6,22,31,33,55,40]

# list=[10,3,4,6,22,31,33,55,40]
# sum=0
# for i in list:
#     if i%2==0:
#         sum=sum+i
# print(sum)    

#3.Wap to find the sum of only odd elments in the list : [10,3,4,6,22,31,33,55,40].

# list=[10,3,4,6,22,31,33,55,40]
# sum=0
# for i in list:
#     if i%2!=0:
#         sum=sum+i
# print(sum)

## 4.Wap to find the count of how many int value and how many str in the list 

list=[70,"aman",50,10,20,"rohan","iq-india"]
int1=0
str1=0
for i in list:
    if type(i)==int:
        int1+=1
    elif type(i)==str:
        str1+=1
print(int1)
print(str1)            
