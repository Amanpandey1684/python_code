'''Write a Python
Program to calculate the sum of all the even numbers in a user given list.
Sample input
2 4 5 6 7 8
Sample output
20'''

num=[2,4,5,6,7,8]

sum=0
for i in range(6):
    if num[i]%2==0:
        sum=sum+num[i]
        print(sum)