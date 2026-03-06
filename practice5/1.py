def simple_generator(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
        
n=int(input())
my_gen = simple_generator(n)
for i in my_gen:
    if i==n or i==n-1:
        print(i)
    else:
        print(i,end=",")
