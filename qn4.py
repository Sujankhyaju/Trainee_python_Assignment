# Write a Python program to reverse a string.

# def reverseString(ipst):
#     return ipst[::-1]

def main():
    input_str = input("Enter a string::  ")
    str1 = ''
    count = len(input_str)-1
    for i in range(count,-1,-1):
        str1 = str1 + input_str[i]        
    print(str1)


if __name__=='__main__':
    main()

