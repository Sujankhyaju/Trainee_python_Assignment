# 5.	A = [‘a’,’b’,’c’,’d’] B = [‘1’,’a’,’2’,’b’]
# Find  (A union B) and (A intersection B)

A = ['a','b','c','d'] 
B = ['1','a','2','b','c']

c = list(set(A+B))
print("The Union of A and B is", c)

d = [item for item in A if item in B]
# for item in A:
#     if item in B:
#         d.append(item)
print("The intersection of A and B is", d)

