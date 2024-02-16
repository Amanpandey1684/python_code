'''WPP TO PRINT THE CUBES OF EVEN NO. BETWEEN THE USER RANGE'''

r1=int(input("enter the no.: "))
r2=int(input("enter the no.: "))
l=[i**3 for i in range(r1,r2) if i%2==0]
print(l)