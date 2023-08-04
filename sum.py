# Task :6 ;Calculate the sum of three given numbers, if the values are equal then return thrice of
# their sum

a=int(input("enter first number:"))
b=int(input("enter second number"))
c=int(input("enter third number:"))

sum=0
sum=a+b+c
print("sum of 3 no is :",sum)
if a==b and b==c:
    print("now value is:",3*sum)
