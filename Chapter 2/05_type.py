# By using type function we can use and write any type of variables.
# and change the variable to other variable if valid 

a = "Harry"
t = type(a)
print(t)

b = 0.31
c = type(b)
print(c)

b = 31
c = type(b)
print(c)

# and change the variable to other variable if valid

a = "31.2" #type string becouse using "" for string
b = float(a) # a but the type of should be float
t= type(b)
print(t)