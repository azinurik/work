def simple_generator(n):
    for i in range(len(n)-1,-1,-1):
        yield n[i]
n=input()
my_gen = simple_generator(n)
for i in my_gen:
        print(i,end="")