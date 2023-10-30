

# problem 2

# n =int(input())
# count =0
# arr= list(map(int,input().split()))
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#
# for i in range(len(arr)):
#     if arr[i]>50:
#         count = count+1
#
# print(" ".join(map(str, arr)))
# print(count)


# problem 3
# n = int(input())
# arr = list(map(int,input().split()))
# count =0
# count1 =0
# arr.sort()
#
# for i in range(0,len(arr)):
#     if arr[i]%2 == 0:
#         i+=1
#         count+=1
#     elif arr[i]%2 == 1:
#         i+=1
#         count1+=1
# if count == n or count1 == n:
#     print("Yes")
# else:
#     print("No")

# n = int(input("Enter an integer: "))
# if 1 <= n <= 100:
#     if n % 2 == 0:
#         print("YES")
#     else:
#         print("NO")
#
#
# w = int(input())
# if w >= 1 and w<=100 and w % 2 == 0:
#     print("YES")
# else:
#     print("NO")

n1 = int(input())
n2 = int(input())
if n1%2==1 and n2%2==1:
    print("Yes")
else:
    print("NO")