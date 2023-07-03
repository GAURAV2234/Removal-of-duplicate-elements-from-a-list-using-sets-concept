## remove duplicate elements from list using a set

a=[]
b=int(input("Enter the No. of elements you want to put in list:"))
for i in range(b):
    b=int(input("Enter element"))
    a.append(b)

print("List you entered with or without dulicate elements: ",a)
s=set(a)
c=list(s)
print("List after removal dulicate elements: ",c)
