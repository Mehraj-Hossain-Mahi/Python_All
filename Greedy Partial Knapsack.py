price = [100,60,200]
weight = [20,10,40]
capacity = 50
def partial_kanpsack(price,weight, capacity):
    items = []
    for p, w in zip(price,weight):
        t = (p/w, p, w)
        items.append(t)
    print(items)
    items.sort(key = lambda x:x[0], reverse=True)
    total_profit =0

    for item in items:
        u = item[0]
        p = item[1]
        w = item[2]

        if w<=capacity:
            total_profit = total_profit+p
            capacity = capacity-w
        else:
            total_profit = total_profit+capacity*u
            capacity =0
            break
    return total_profit
print(partial_kanpsack(price,weight,capacity))



