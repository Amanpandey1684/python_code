#. Program to find the number of currency notes of each type (Rs. 2000, Rs. 500 and Rs. 100),
#when the total number of currency notes counted altogether is minimum and there must be at
# least a 100 rupee note dispensed. The amount to be withdrawn is to be entered by the user


a=int(input("enter the amount"))
a=a-100
tt=a//2000
a=a%2000
fh=a//500
a=a%500
th=a//200
a=a%200
h=a//100
a=a%100
h=h+1
print('2000=',tt,'\n500',fh,'\n200',th,'\n100',h)