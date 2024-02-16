''' write a python program to take a string from user and then check it is a pangram or not '''


s=input("take input from user: ")
s=s.lower()
for i in range(97,123):
    if chr(i) not in s:
        print("not a pangram")
        break
else:
    print("it is a pangram")    
