
def FirstFit(products,target):
    res = 0
    bin_rem = [0]*len(products)
    for p in products:
        j = 0
        while(j<res):
            if bin_rem[j]>=p:
                bin_rem[j]-=p
                break
            j+=1
        if j==res:
            bin_rem[j]=target-p
            res+=1
    return res
products = [6,3,2,4,1,5]
target = 7
print("Minimum Bus Need : ",FirstFit(products,target))



def FirstFit_Decreasing(products,target):
    res = 0
    products.sort(reverse=True)
    bin_rem = [0]*len(products)
    for p in products:
        j = 0
        while(j<res):
            if bin_rem[j]>=p:
                bin_rem[j]-=p
                break
            j+=1
        if res==j:
            bin_rem[res]= target-p
            res+=1
    return res
products = [6,3,2,4,1,5]
target = 7
print("Minimum Bus Need : ",FirstFit_Decreasing(products,target))



def GreedyCoinChange(coins,target):
    coins.sort(reverse=True)
    res = 0
    for c in coins:
        if target//c >0:
            r= target//c
            res+=r
            target = target-r*c
    if target==0:
        return res
    else:
        return "Not Possible"
products = [20,10,5,2,1]
target = int(input())
print(GreedyCoinChange(products,target))



def Next_Fit(products,target):
    res = 1
    c = target
    for p in products:
        if target - p >=0:
            target-=p
        else:
            target = c - p
            res+=1
    return res
products = [6,3,2,4,1,5]
target = 7
print(Next_Fit(products,target))

