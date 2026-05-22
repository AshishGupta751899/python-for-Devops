# #waf to check how many vowel in a string

# def count_vowels(a):
#     count = 0
#     for i in a:
#         if i in "aeiouAEIOU":
#             count += 1
#     return count

# res=count_vowels("programming is fun")
# print("Number of vowels in the string:", res)


#local variable and global variable:

# name = "ashish"  # global variable
# def msg():
#     name = "ashish kumar"  # local variable
#     print("local variable:", name)
# msg()
# print("global variable:", name)

# waf to count char "p" in "python programming" return total occurence:

# def count_p(a):
#     count = 0
#     for i in a:
#         if i == "p":
#             count += 1
#     return count
# res = count_p("python programming")
# print("Number of 'p' in the string:", res)

#waf to return sum of string indexes "python"

def count_index(a):
    count = 0
    for i in range(len(a)):
        count=count+i
    return count
res = count_index("python")
print(res)
    