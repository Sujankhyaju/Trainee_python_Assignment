# 8.	Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def main():
    '''
    sorting hyphen-separated words in alphabetical order
    '''
    strg = input("Enter a hyphen-separated words: ").split('-')
    l2= sorted(strg)
    strg = "-".join(l2)
    print(strg)

if __name__ == '__main__':
    main()


