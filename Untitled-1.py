n=int(input("Enter a number:"))
n1=n
n2=n
s=0
c=0
while n>0:
    n=n//10
    c=c+1
while n1>0:
    rem =n1%10
    n1=n1//10
    p=rem**c
    s=s+p
if n2==s:
    print("Armstrong")
else:
    print("Not")
