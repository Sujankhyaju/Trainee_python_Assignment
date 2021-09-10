# Generate the following patterns using for loop
		
    # F
    # FFF
    # FFFFF
    # FFFFFFF
    # FFFFFFFFF
    # FFFFFFFFFFF
# ---------------------------------------------------
    # F
    # F
    # FF
    # FFF
    # FFFFF
    # FFFFFFFF
    # FFFFFFFFFFFFF
# ------------------------------------------------
def pattern1():
    n=1
    for i in range(0,6):
        for j in range(0,n):
            print("F",end='')
        n+=2
        print("\r")

def pattern2():
    n1=0
    n2=1
    for i in range(0,7):
        for j in range(0,n2):
            print("F",end='')
        n3 = n2+n1
        n1 = n2
        n2 = n3     
        print('\r')

def main():
    pattern1()
    pattern2()

if __name__ == '__main__':
    main()