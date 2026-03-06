n=int(input())
for i in range(n+1):
    if i&i-1==0 and i!=0:
        print(i, end=" ")