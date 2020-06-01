n1=int(input("enter the number of elements in list 1:"))
l1=[]
for i in range(n1):
    l1.append(input())
n2=int(input("enter the number of elements in list 2"))
l2=[]
for i in range(n2):
    l2.append(input())
print("intersection is",set(l1).intersection(set((l2))))    
