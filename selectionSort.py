
a=[12,3,13,2,5,7,6,22,21]
length=len(a)
for i in range(length):
    index=i
    for j in range(i+1,length):
        if(a[j]<a[index]):
            index=j
    temp=a[i]
    a[i]=a[index]
    a[index]=temp
print(a)
