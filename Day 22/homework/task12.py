"""12. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს ხმოვანი ასოების რაოდენობას string'ში."""


def vowels_count(string):
    vowels = "aeiou" 
    for char in string:
        if char in vowels:
            count = count + 1
    return count