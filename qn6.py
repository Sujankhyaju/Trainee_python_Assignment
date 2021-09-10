# 2.	Write a program to calculate direction and magnitude of the vector described by the following points. 
# A = (20,30) and B = (30,40)

import math

A = (20,30)
B = (30,40)

result = (B[0]-A[0],B[1]-A[1])
print(f"Given Vectors are {A} and {B}")
print("resultant vector is ",result)

magnitude = math.sqrt(pow(result[0],2)+pow(result[1],2))
print("magnitude of resultant is ",magnitude)

direction = math.atan(result[1]/result[0])
degree = direction * 180 / math.pi
print("Direction of resultant vector is ",degree)
