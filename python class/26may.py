#Data structure.
#Data structure used to store data effectively and make faster 
# for operations like Read and write.
#1. String  : str()
#2.list : kist()
#3.dictionary: dict()
#4.set:set()
#5.tuple: tuple()


#list is a data structure in python used to store multiple data in of different types in one variable.
#1.list can be defined by [] and data inside known as element.
# marks_10th=[20,55,60,76,50,60]
#2.list can  be heterogenious and homogeneous
#3.list are mutable(changed)
#4.list support indexing , slicing and follows ordering sequence.


#list and its property
#1. Creation of list
#2.updation of list
#3.indexing
#4.slicing
#5.traversing
#6. In-built method
#7.Test
#8.Assignment

# example :
marks_10th=[20,55,60,76,50,60]
print("before update : marks_10th")
marks_10th[-1]=200 #mutating list index using index
print("after updting :" ,marks_10th)


n=7
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print("*" , end=" ")
        else:
            print(" " ,end=" ")
    print( )
        