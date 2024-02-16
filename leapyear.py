''' wapp to take a year no. from user and print it is a leap year'''
Year=int(input("enter the year: "))
if (Year%400==0) or (Year%100!=0) and (Year%4==0):
    print("The year is the leap year")
else:
    print("The year is not a leap year")    