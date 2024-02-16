'''wapp to take three no. from user and print the graetest no.'''

a=int(input("enter the first no.: "))
b=int(input("enter the second no.: "))
c=int(input("enter the third no.: "))

if (a>b) and (a>c):
    print(f"{a}is greatest no.")
elif (b>a) and (b>c):
    print(f"{b}is the greatest no.")
elif (c>a) and (c>a):
    print(f"{c}is the greatest no.")        