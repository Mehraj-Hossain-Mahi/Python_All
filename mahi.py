arr = list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)
print(" ".join(map(str, arr)))


for i in range(len(arr)):
    min = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min]:
            i+=1
    arr[i],arr[min]=arr[min],arr[i]
print(arr)

for i in range(len(arr)):
    key = arr[i]
    j = i-1
    while j>0 and arr[j]>=key:
        arr[j+1],arr[j]=arr[j],arr[j+1]
        j-=1
    arr[j+1]=key
print(arr)

def partition(arr,low,high):
    i = low
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <=pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[high]=arr[high],arr[i]
    return i

def quicksort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

a = list(map(int,input().split()))
quicksort(a,0,len(a)-1)
print(a)


def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid= len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    sortedleft = mergesort(left)
    sortedright = mergesort(right)
    i,j=0,0
    sortedarr=[]

    while i<len(sortedleft) and j <len(sortedright):
        if sortedleft[i] < sortedright[j]:
            sortedarr.append(sortedleft[i])
            i+=1
        else:
            sortedarr.append(sortedright[j])
            j+=1
    return sortedarr+sortedright[j:]+sortedleft[i:]

a = list(map(int,input().split()))
print(mergesort(a))
