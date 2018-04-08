
a=[20,12,18,3,8,6,4,19,14]
length=len(a)
for i in range(length-1):
	for j in range(length-1-i):
		if a[j]>a[j+1]:
			temp = a[j]
			a[j]=a[j+1]
			a[j+1]=temp
print(a)
			
