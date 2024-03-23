class car_show_room:
    def __init__(self):
        self.cgst=565
        self.sgst=666
        self.insurance=988
    def company(self,name):
        while True:
            name=input("select the company : ") 
            if name=="suziki":    
                print("welcome to ",name,"company")
                self.f=name 
                break
            elif name=="tata":
                print("welcome to ",name,"company")
                self.f=name 
                break
            elif name=="mahendhra":
                print("welcome to ",name,"company")
                self.f=name
                break
            else:
                print("please enter again")
                self.f=name        
    def model(self,m):
        while True:
            print("select the model in ",m,"company")
            models=[["dzire","swift"],["crystal","inova"],["thar","xuv"]]
            m=input("select the model:")
            if m=="suziki":
              print(models[0])
              break
            elif m=="tata":
              print(models[1])
              break
            elif m=="mahendhra" :
              print(models[2])
              break
            else:
              print("enter again")
    def price(self,t):
        if t=="dzire":
            a=100000
            print("the  dzire price is ",a)
            f_price=a+self.cgst+self.sgst+self.insurance
            print("the on ride price is ",f_price)
        elif t==("swift"):
            b=200000
            print("the swift price is:",b)
            f_price=b+self.cgst+self.sgst+self.insurance
            print("the on ride price is :",f_price)
        elif t=="crystal":
            c=300000
            print("the crystal price is:",c)
            f_price=c+self.cgst+self.sgst+self.insurance
            print("the on ride price is ",f_price)
        elif t=="inova":
            d=5000000
            print("the inova price is ",d)
            f_price=d+self.cgst+self.sgst+self.insurance
            print("the on ride price is ",f_price)
        elif t=="thar":
            e=7800000
            print("the thar price is ",e)
            f_price=e+self.cgst+self.sgst+self.insurance
            print("the on ride price is ",f_price)
        elif t=="xuv":
            f=9000000
            print("the xuv price is 8800000")
            f_price=f+self.cgst+self.sgst+self.insurance
            print("the on ride price is ",f_price)
                   
companies=["suziki","tata","mahendhra"]
print(companies)      
n=input("select the company : ")    
o=car_show_room()
o.company(n)
o.model(n)
p=input("select the model:")
o.price(p)