def simple_generator(n):
    for i in range(0,n+1):
            yield 2**i
        
n=int(input())
my_gen = simple_generator(n)
for i in my_gen:
        print(i,end=" ")
