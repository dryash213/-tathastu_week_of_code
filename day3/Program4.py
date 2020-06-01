n=int(input("enter the number of elements"))
l=[]
for i in range (n):
    l.append(input())
print(l)
def duplicate(l):
    duplicatelist=[]
    for i in l:
        if i not in duplicatelist:
            duplicatelist.append(i)
    return(duplicatelist)
print(duplicate(l))
