'''take the month no. from user and print no. of days from user
sample input:
3
sample output:
31 '''

month=int(input('Enter the month no.'))
days=(month<=7)*(30+(month%2))+(month>7)*(31-(month%2))-2*(month==2)
print(f"The days in month: {days} ")