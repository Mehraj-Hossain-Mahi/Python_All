def partition(arr,low,high):
    i = low
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
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

