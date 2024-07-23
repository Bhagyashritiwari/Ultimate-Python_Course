# Write a program to find out whether a given post is talking about “Bani” or not

post = input("Enter the post:")

if("Bani"and "Nisar".lower() in post.lower()): # by using lower() in python we are able to print lower case string bani
    print("This post is all about Bani, and nisar")

else:
    print("This post is not about the Bani")    