print("Enter a Array all number ,write sequentially  : ")
a = list(map(int,input().split()))
n = int(input("Enter the Element For seaching : "))
flag = False
for i in range(len(a)):
    if a[i]==n:
        print("Found")
        flag = True
        break
if flag == False:
    print("Not Found")
