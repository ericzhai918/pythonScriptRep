a=[22,44,1,3,4,77,32,45,18,2]
length = len(a)
for i in range(1, length):
    key = a[i]
    j = i - 1
    while j >= 0:
        if a[j] > key:
            a[j + 1] = a[j]
            a[j] = key
        j -= 1
print(a)

