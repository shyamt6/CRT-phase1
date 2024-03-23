list=[42,36,28,96,4,-1,1]
min=999
for i in range(0,len(list)):
    if list[i]<min:
        min=list[i]
print(min)
max=-999
for i in range(0,len(list)):
    if list[i]>max:
        max=list[i]
print(max)
print(min+max)
