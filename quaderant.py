'''wapp to take cordinates(x and y) of the points from user and find in which quadrent that point lies'''

x=int(input("Enter the 1st cordinate: "))
y=int(input("Enter the 2nd cordinate: "))

if (x>0) and (y>0):
    print("the no. is in first quadrent")
elif (x<0) and (y>0):
    print("the no. is in second quadrent")
elif (x<0) and (y<0):
    print("the no. is in third quadrent")
elif (x>0) and (y>0):
    print("the point in fourth quadrent") 