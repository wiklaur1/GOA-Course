"""2) შექმენით ისეთ პროგრამა რომელიც მომხმარებელს შემოატანინებს 2 რიცხვს. შემოტანის შემდეგ for loop ის მეშვეობით გამოთვალეთ ყველა 
რიცხვი ამ ორ რიცხვს შორის და შემდეგ ისიდი ჩაამატეთ ლისტში საბოოლოოდ კი დაპრინტეთ ტერმინალში"""


num1 = input("enter your first number: ")
num2 = input("enter your second nummber: ")
num_list = []
if num1>num2:
    for num in range(num2,num1):
        num_list.append(num)
else:
    for num in range(num1,num2):
        num_list.append(num)
print(num_list)