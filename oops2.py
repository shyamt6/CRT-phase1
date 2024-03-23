class shopping:
    def dress_type(self,type):
        self.s1=type
    def dress_price(self,price):
        self.s2=price
    def dress_size(self,size):
        self.s3=size
    def display(self):
        print(self.s1)
        print(self.s2)
        print(self.s3)

Man=shopping()
Man.dress_type("jeans")
Man.dress_price(100)
Man.dress_size("l")
Man.display()
