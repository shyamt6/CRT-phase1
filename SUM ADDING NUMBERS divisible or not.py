n=47
sum=0
m=n
while n>0:
        digits=n%10
        sum=sum+digits
        n=n//10
print(sum)
if m%sum==0:
        print("it is divisible")
else:
        print(" NOT DIVISIBLE")

