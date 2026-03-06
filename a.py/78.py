s = "ab anjvna b knvlakns za knvlksan"
a= list(map(str,s.split()))
d={}
for i in range(len(a)):
    if "a" in a[i]:
        d[i]=a[i]
print(d)
#{
#  1:"ab"
#  2: "anjvna"
#...  
#}

