"""3) შექმენით პროგრამა სადაც მომხმარებელი შემოიტანს ორ რიცხვს საწყისი რიცხვი და ბოლო რიცხვი, გამოიანგარიშეთ ამ რიცხვებს შორის 
ყველა რიცხვი და დაამატეთ სიაში, საბოლოოდ დაბეჭდეთ ამ სიიდან მაქსიმალური, 
მინიმალური და ყველა რიცხვის ჯამის მნიშნელობები"""


num1 = input("enter your first number: ")
num2 = input("enter your second nummber: ")
num_list = []
if num1>num2:
    for num in range(num2,num1):
        num_list.append(num)
else:
    for num in range(num1,num2):
        num_list.append(num)
print(num_list[0])
print(num_list[len(num_list)-1])
