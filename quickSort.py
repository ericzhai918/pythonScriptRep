def quickSort(a,left,right):
    if left>=right:
        return a
    key=a[left]
    low=left
    high=right
    while left < right:
        while left<right and a[right]>=key:
            right -= 1
        a[left]=a[right]
        while left<right and a[left]<=key:
            left += 1
        a[right]=a[left]
    a[right]=key
    quickSort(a,low,left-1)
    quickSort(a,left+1,high)
    return a

a=[6,1,2,7,9,3,4,5,10,8]
print(quickSort(a,0,len(a)-1))
