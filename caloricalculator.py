#python code for calculation of caloricalculation
Gender=input("Enter your gender: ")
bodyweight=int(input("Enter the bodyweight: "))
height=int(input("Enter the heght: "))
age=int(input("Enter the age: "))

male=66.5+(13.75*bodyweight)+(5.003*height)-(6.75*age)
female=655.1+(9.563*bodyweight)+(1.850*height)-(4.676*age)

print(f'calori of male is: {male}: ')
print(f'calori for felmale is: {female}: ')