"""9. შექმენით ფუნქცია, რომელიც იღებს 2 integer'ების list'ს და აბრუნებს ორივე list'იდან მინიმალური რიცხვების სხვაობას."""


def min_subtraction(list1,list2):
    return min(list1)-min(list2)


print(min_subtraction([1,2,3],[4,6,7]))
