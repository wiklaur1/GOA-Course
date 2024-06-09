"""შექმენით პროგრამა სადაც მომხმარებელს შემოატანინებთ ორ რიცხვს და თუ 
პირველი რიცხვი იქნება მეორე რიცხვზე მეტი დაბეჭდეთ პირველი რიცხვი, 
ხოლო სხვა შემთხვევაში დაბეჭდეთ მეორე რიცხვი"""


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1)
else:
    print(num2)