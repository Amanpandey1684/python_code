'''' WAPP TO PRINT THE NUMBERS THAT IS NEITHER DIVISIBLE BY THREE NOR THE NO. 
      ENDS WITH THE LAST DIGIT 3'''
      
a=int(input("Enter the no.: "))
for i in range(1000):
    if i%3!=0 and i%10!=0:
        print(i)