

def FirstFit(products,target):
    res = 0
    bin_rem = [0]*len(products)
    for p in products:
        j = 0
        while(j<res):
            if bin_rem[j] >= p:
                bin_rem[j] = bin_rem[j] - p
                break
            j+=1
        if (j==res):
            bin_rem[res] = target - p
            res+=1
    return  res
products = [2,6,3,5,4,1]
target = int(input())
print("Minimum Bus : ",FirstFit(products,target))

def FirstFit_decreasing(products, target):
    products.sort(reverse=True)
    res = 0
    bin_rem = [0]*len(products)
    for p in products:
        j = 0
        while(j<res):
            if bin_rem[j] >= p:
                bin_rem[j] = bin_rem[j] - p
                break
            j+=1
        if (j==res):
            bin_rem[res] = target - p
            res+=1
    return  res
products = [3,1,6,4,5,2]
target = int(input())
print("Minimum Bus : ",FirstFit_decreasing(products,target))
