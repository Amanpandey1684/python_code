#take two no. from user and then find the greatest no.
a=int(input("Enter the no.: "))
b=int(input("entr the no.: "))
c=(a>b)*a + (b>a)*b
print(f'greastest no. is: {c}')