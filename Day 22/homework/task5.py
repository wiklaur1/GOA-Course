"""5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome 
(ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს."""


def palindrome(word):
    if word==word[::-1]:
        return True
    return False

print(palindrome("giorgi"))
print(palindrome("wow"))



