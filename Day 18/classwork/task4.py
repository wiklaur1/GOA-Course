"""4) შექმენით პროგრამა სადაც მომხმარებელს შეეკითხებით რამდენი რიცხვის შემოტანა სურს შემდეგ კი for ციკლის 
მეშვეობით იმდენჯერ შემოატანინეთ რიცხვი რამდენიც მიუთითა ამის შემდეგ ეს რიცხვები დაამატეთ სიაში 
და საბოლოოდ გამოიტანეთ ამ რიცხვების ჯამი"""


amount = int(input("please enter amount of numbers: "))
num_list = []
for i in range(amount):
    num = int(input("enter number: "))
    num_list.append(num)
sum = 0
for num in num_list:
    sum = sum + num
print(sum)