a=int(input())
n=list(map(int,input().split()))
s=n[0]
for c in n:
    if s<c:
        s=c
print(s)