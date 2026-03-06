a=int(input())
n=list(map(int,input().split()))
s=n[0]
d=1
for i in range (1,a):
    if s<n[i]:
        s=n[i]
        d=i+1
print(d)