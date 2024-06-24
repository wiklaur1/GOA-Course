"""6) https://www.w3schools.com/python/python_conditions.asp გააკეთეთ 5 მაგალითი if-else"""


#1
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
if num1>num2:
    print("first number is greater then second number")
else:
    print("first number isn't greater then second number")
#2
if 8>7:
    print("hello world")
else:
    print("good bye world")
#3
a = "gio"
b = "giorgi"
if a==b:
    print("giorgi")
else:
    print("gio")
#4
login = input("enter your password: ")
password = "gio123"
if login == password:
    print("access granted")
else:
    print("access denied")
#5
age =int(input("enter your age: "))
if age > 18:
    print("you are adult")
else:
    print("you are not adult")