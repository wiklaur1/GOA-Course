"""6. შექმენით ფუნქცია, რომელიც პოულობს ყველაზე გრძელ string'ს string'ების სიაში."""


def longest_string(list1):
    len_list=[]
    for i in range(len(list1)):
        len_list.append(len(list1[i]))
    longest = max(len_list)
    index = 0
    for i in range(len(len_list)):
        if len_list[i]==longest:
            index = i
    return list1[index]
        


print(longest_string(["giorgi","saba","nika","luka","jemaliko","petre","pavle"]))



