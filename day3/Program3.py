s=input("enter the string")
def duplicate(s):
    duplicatestring=""
    for i in s:
        if i not in duplicatestring:
            duplicatestring += i
    return duplicatestring
print(duplicate(s))
