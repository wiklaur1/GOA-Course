"""11. შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს და აბრუნებს ყველა ელემენტის ჯამს."""


def sum(arr):
    sum = 0 
    for num in arr:
        sum = sum + num 
    return sum