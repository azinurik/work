def simple_generator(n,m):
    for i in range(n,m+1):
        yield i**2
        
n,m=map(int,input().split())
my_gen = simple_generator(n,m)
for i in my_gen:
        print(i)
