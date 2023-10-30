def greedycoinchange(coins,ammount):
    res = 0
    coins.sort(reverse=True)
    for coin in coins:
        if ammount//coin>0:
            r = ammount//coin
            res+=r
            ammount = ammount- r*coin
    if ammount==0:
        return res
    else:
        return "Not Possible"

print("Enter the all note")
coins = list(map(int,input().split()))
print("Enter the ammount: ")
ammount = int(input())
print("Note are : ",coins)
print("Minimum Note need : ",greedycoinchange(coins,ammount))