n,l,r=map(int,input().split())
n=list(map(int,input().split()))
l=l-1
n[l:r]=reversed(n[l:r])
for c in n:
    print(c,end=" ")
