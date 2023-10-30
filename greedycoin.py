def greedy_coin_Exchange(coins,ammount):
    res = 0
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

coins1 = [10,20,50,5,2,1,3]
ammount = int(input())
print(greedy_coin_Exchange(coins1,ammount))