def prime():
    f=1
    a=int(input("enter the  number:"))
    for i in range(2,a):
        if a%i==0:
            f=0
            break
    if f==1:
            print("it is prme")
    else:
         print("not prime")
prime()
              