"""
4) მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი, 
საცხოვრებელი ადგილი და მეილი. ყველა შეინახეთ ცვლადებში და შემდეგ ჩაამატეთ სიაში, საბოლოოდ კი დაბეჭდეთ ეს სია."""


data = []
name = input("enter your name: ")
data.append(name)
surname = input("enter your surname: ")
data.append(surname)
age = int(input("pleas enter your age: "))
data.append(age)
address = input("please enter your address: ")
data.append(address)
mail = input("please enter your mail: ")
data.append(mail)

print(data)
