arr = list(map(int,input().split()))
key = int(input())
left = 0
right = len(arr)-1
flag = False

while(left<=right):
    mid = (left+right)//2

    if key>arr[mid]:
        left = mid+1
    elif key<arr[mid]:
        right = mid-1
    else:
        print("Found")
        flag = True
        break
if flag == False:
    print("Not Found")
