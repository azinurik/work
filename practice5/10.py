def simple_generator(n,m):
    for i in range(m):
        for j in range(len(n)):
            yield n[j]
        
n=list(map(str,input().split()))
k=int(input())
my_gen = simple_generator(n,k)
for i in my_gen:
        print(i,end=" ")