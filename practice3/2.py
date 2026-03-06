def isUsual(n):
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1


n = int(input())

if isUsual(n):
    print("Yes")
else:
    print("No")