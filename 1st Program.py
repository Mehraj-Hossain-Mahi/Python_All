# print("61_O")
# section = 61
# sec = str(section)
# print(sec)
# print(type(sec))
# print(type(section))
# l = list(2, 1, 6654)
# l.append(4)
# l.remove(1)
# print(l)
# m = input()
# print(m)
# print(type(m))
# print(l[i])
# if l[i] == 1:
#     print("One")
# elif l[i] == 2:
#     print("Two")
# else:
# print("None")
#

# l = list([4,2,3,5])
# print(l)
# searchkey= input()
# flag = False
# for i in range(0, len(l)):
#     if l[i] == searchkey:
#         print("Found")
#         flag = True
#         break
# if flag == False:
#     print("Not Found")

# l = list([1,3,2,4,5,6,7,23,55,254,6632,653])
# print(l)
# skey = 3
# flag = False
# for i in range(0,len(l)):
#     if l[i] == skey:
#         print("Found the key")
#         flag = True
#         break
# if flag == False:
#     print("The key is not found")
#
# l1 = list([12,3,24,25,24,63,43,26,32,80])
# print(l1)
# search = 22
# flag = False
# for i in range (0,len(l1)):
#     if l1[i] == search:
#         print("Found")
#         flag = True
#         break
# if flag == False:
#     print("Not Found")
#

# l2 = list([23,4,2,4,5,2,4])
# sr = 4
# flag = False
#
# for i in range (0,len(l2)):
#     if l2[i] == sr:
#         print("Found")
#         flag = True
#         break
# if flag == False:
#     print("Not Found")

print("Enter all elements for Linear Search : ")
l = list(map(int,input().split()))
print(l)

key = int(input("Enter a key to search : "))
flag = False

for i in range(0,len(l)):
    if l[i] == key:
        print("Found Yor Key")
        flag = True
        break
if flag == False:
    print("Not Found")











