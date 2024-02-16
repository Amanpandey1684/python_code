#Write a python program to find the intersection between two tuples.
#sample input       sample output
#(2, 4, 7, 9)       (4, 9)
#(4, 6, 8, 9)

t1=(2,4,7,9)
t2=(4,6,8,9)
intTuple=tuple(set(t1)&set(t2))
print(str(intTuple))