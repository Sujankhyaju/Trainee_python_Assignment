# 8.	Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

strg = input("Enter a hyphen-separated words: ").split('-')
l2= sorted(strg)
strg = "-".join(l2)
print(strg)



# 11.	Write a program to double a given number and add two numbers using lambda()?

num = int(input("Enter a number: "))
db = lambda num : num*2
ad = lambda a,b : a+b
print("twice value of {} is {} ".format(num,db(num)))
print("Addition of 3 and 5 is ",ad(3,5))

