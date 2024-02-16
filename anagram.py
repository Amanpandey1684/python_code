'''write a python program to take two string from user and then cj=heck they are anagram or not

eg: 
 blue
 lube '''
 
s1=input()
s2=input()
if sorted(s1)==sorted(s2):
    print("anagram")
else:
    print("not anagram")    

