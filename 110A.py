n=input()
c=0
for i in n:
    if i=="4" or i=="7":
        c=c+1
counter=0
for i in str(c):
    if i=="4" or i=="7":
        counter=counter+1
if counter==len(str(c)):
    output="YES"
else:
    output="NO"
print(output)