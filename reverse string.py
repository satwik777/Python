def reverse(string):
    empstr1=''
    index=len(string)
    while index>0:
        empstr1 += string[index-1]
        index = index - 1
    return empstr1
print(reverse('123abcd'))