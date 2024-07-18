# . Write a program to accept marks of 6 students and display them in a sorted
# manner.

Students = []

f1 = int(input("Enter Marks here: "))
Students.append(f1)
f2 = int(input("Enter Marks here: "))
Students.append(f2)
f3  = int(input("Enter Marks here: "))
Students.append(f3)
f4 = int(input("Enter Marks here: "))
Students.append(f4)
f5 = int(input("Enter Marks here: "))
Students.append(f5)
f6 = int(input("Enter Marks here: "))
Students.append(f6)
Students.sort()
print(Students)