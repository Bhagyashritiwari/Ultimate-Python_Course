# 3. Attempt problem 1 using while loop
# 1. Write a program to print multiplication table of a given number using for loop.

num = int(input("Enter a number :"))
i =1
while(i<11):
    print(f"{num} *{i} = {num*i}")
    i+=1
