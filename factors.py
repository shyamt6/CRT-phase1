n=12
sum=0
for i in range(1,n):
    if n%i==0:
        print(i)
        sum=sum+i
print(sum)
if sum>n:
    print(" it is greater")
else:
    print(" it is not grater  ")
