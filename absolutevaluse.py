#take an integer from user and print its absolute
#sample input
# -5
#sample output
# 5

a=int(input("Enter the value: "))

b=(a>0)*a+(a<0)*-a
print(f'Absolute vale is: {b}')