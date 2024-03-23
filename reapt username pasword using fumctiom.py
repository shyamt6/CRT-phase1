def login():
    f=1
    while f!=0:
        username=input("enter the username:")
        pasword=input("enter password:")
        if username==pasword:
            print("sucess")
            break
        else:
            print("tryagain")
login()
