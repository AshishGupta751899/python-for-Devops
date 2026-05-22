# Wap to sum of the indices of a string :"python"

name = "python"
total = 0
for i in range(len(name)):
    total+= i
    print(total)

#wap to print the factorial from 1 to 8

for i in range(1, 9):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    print(f"Factorial of {i} is {factorial}")

# wap to print only prime numbers from 1 to 15

for num in range(1, 16):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)