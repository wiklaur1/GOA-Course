""" განიხილეთ და კომენტარებით ახსენით როგორ მუშაობს გაკვეთილზე დაწერილი კოდი:"""

def find_short(s):
    #creating words list
    list1 = s.split(" ")

    #creating variable with lenght of first word as its value
    word_len = len(list1[0])
    for i in list1:
        #cheking if other word is shorter than firs one
        if len(i) < word_len:
            word_len = len(i)
    
    # word_len = 3
    return word_len

print(find_short("bitcoin take over the world maybe who knows perhaps"))

