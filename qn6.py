# 2.	Write a program to calculate direction and magnitude of the vector described by the following points. 
# A = (20,30) and B = (30,40)

import math

def magnitude(result):
    '''
    calculate the magnitude of resultant vector
    '''
    return  math.sqrt(pow(result[0],2)+pow(result[1],2))

def direction(result):
    '''
    calculate direction of resultant vector and converted into degree
    '''
    result = math.atan(result[1]/result[0])
    return  result * 180 / math.pi

def main():
    A = (20,30)
    B = (30,40)
    result = (B[0]-A[0],B[1]-A[1])
    print(f"Given Vectors are {A} and {B}")
    print("\nResultant vector is ",result)
    print("\nMagnitude of resultant is ",magnitude(result))
    print("\nDirection of resultant vector is ",direction(result))

if __name__ == '__main__':
    main()
