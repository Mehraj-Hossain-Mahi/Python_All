def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)


def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)

print(factorial(int(input("Enter the value of N: "))))
print(sum(int(input("Enter the value of N: "))))