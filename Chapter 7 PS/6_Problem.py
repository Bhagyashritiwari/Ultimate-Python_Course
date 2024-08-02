# # 6. Write a program to calculate the factorial of a given number using for loop.

# 5!

n = int(input("Enter factorial num:"))
product = 1
for i in range(1, n+1):
    product = product * i
   
 
print(f"The Factorial of {n} is {product}")