# Write a Python program to reverse a string.

input_str = input("Enter a string::  ")

# print(input_str[::-1])

str1 = ''
count = len(input_str)-1
for i in range(count,-1,-1):
    str1 = str1 + input_str[i]
    
print(str1)

print("------------------------------------------------------------------------------------------")

