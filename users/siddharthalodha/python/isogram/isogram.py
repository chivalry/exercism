import re

def is_isogram(string):
    string="".join(ch for ch in string if ch.isalnum())
    print(string)
    string=string.strip().lower()
    list1=[i for i in string]
    set1=set(list1)
    if(len(list1)!=len(set1)):
        return False
    return True
