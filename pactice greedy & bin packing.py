
def greedy(coins,ammount):
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
coins = [20,1,2,10,5]
ammount = int(input())
print(greedy(coins,ammount))



def Nextfit(products,target):
    res = 1
    c = target
    for p in products:
        if target - p>=0:
            target = target - p
        else:
            res+=1
            target = c - p
    return res
products = [6,3,2,4,1,5]
target = 7
print("Minimum Bus Need : ",Nextfit(products,target))


def FirstFit(products,target):
    res = 0
    bin_rem = [0]*len(products)
    for p in products:
        j = 0
        while(j<res):
            if bin_rem[j]>= p:
                bin_rem[j]-=p
                break
            j+=1
        if (j==res):
            bin_rem[res]= target - p
            res+=1
    return res
products = [2,6,3,5,4,1]
target = int(input())
print("Minimum Bus : ",FirstFit(products,target))


def First_Fit_Decreasing(products,target):
    products.sort(reverse=True)
    res = 0
    bin_rem = [0] * len(products)
    for p in products:
        j = 0
        while(j<res):
            if bin_rem[j] >= p:
                bin_rem[j]-=p
                break
            j+=1
        if j==res:
            bin_rem[res] = target - p
            res+=1
    return res

products = [2,6,3,5,4,1]
target = int(input())
print("Minimum Bus : ",First_Fit_Decreasing(products,target))

