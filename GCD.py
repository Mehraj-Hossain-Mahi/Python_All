def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)

a = int(input("Enter the Value of A: "))
b = int(input("Enter the value of B: "))

print(gcd(a,b))


