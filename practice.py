def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def selectionsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
    arr[i],arr[min]=arr[min],arr[i]
    return arr


def insertionsort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr



def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    sortedleft = mergesort(left)
    sortedright = mergesort(right)

    i,j = 0,0
    sortedarr=[]

    while (i<len(sortedleft) and j<len(sortedright)):
        if sortedleft[i]<sortedright[j]:
            sortedarr.append(sortedleft[i])
            i+=1
        else:
            sortedarr.append(sortedright[j])
            j+=1
    return sortedarr+sortedleft[i:]+sortedright[j:]





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




def greedy(coins,ammount):
    res =0
    coins.sort(reverse=True)
    for coin in coins:
        if ammount//coin>0:
            r = ammount//coin
            res+=r
            ammount-=r*coin
    if ammount==0:
        return res
    else:
        return "Not Possible"
coins = [10,20,5,2,50,3,1]



a = list(map(int,input().split()))
quicksort(a,0,len(a)-1)
print(mergesort(a))
print(bubblesort(a))
print(selectionsort(a))
print(insertionsort(a))
print(a)
ammount = int(input())
print(greedy(coins,ammount))