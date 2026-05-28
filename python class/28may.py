#slicing
marks=[10,20,30,40,50,60,70,80]
# [start-0:stop-1:step-1]

sub_list=marks[0:8:2]
print(sub_list)

marks=[10,20,30,40,50,60,70,80]
sub_list=marks[0:8:3]
print(sub_list)

#reverse list
marks=[10,20,30,40,50,60,70,80]
sub_list=marks[0::-1]
print(sub_list)

#6.Traversing
marks=[10,20,30,40,50,60,70,80]
for i in range(len(marks)):
    if marks[i]%2==0:
        print(f"this number is even : {marks[i]}")
    else:
        print(f"this number is odd : {marks[i]}")



marks=[10,20,30,40,50,60,70,80]
total=0
for i in marks:
    total=total+i
print(total)
        