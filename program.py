import math

intvariable= 4
floatvariable= 4.5
stringvariable= "Software 1 is fun"
'''
print(intvariable)
print(floatvariable)
print(stringvariable)

print(type(intvariable))
print(type(floatvariable))
print(type(stringvariable))

#typecasting is fun
intvariable= int(floatvariable)
print("here is the int version of float variable",intvariable)

shareOfLoan= 500.5/3
print(shareOfLoan)
print(int(shareOfLoan))
print(type(shareOfLoan))

num1 =int(input("Enter a number"))
num2 =float(input("Enter another number"))
sum =num1 + num2
print(sum)

name = input("Enter your name")
school = input("Enter your school")

print(" you are: ", name, "and your school name is : ", school)
print(f"you name is {name}, and school is {school}")
print(f" you name is {name}, and you float variable is ,{floatvariable}")
print(f" you name is {name}, and you float variable is ,{floatvariable:.2f}")
'''

rds = float(input("Enter RDS"))
area = math.pi * (rds ** 2)
print(f" you RDS is {rds}, and area is, {area:.2f}")