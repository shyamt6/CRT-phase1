class shopping:
    def __init__(self,place):
        self.p=place
        print("wlcm to shopping at ",place)
    def dress_type(self,type):
        self.s1=type
    def dress_price(self,price):
        self.s2=price
    def dress_size(self,size):
        self.s3=size
    def display(self):
        print("dress type",self.s1)
        print("dress price",self.s2)
        print("dress size",self.s3)


Man=shopping("TJS")
Man.dress_type("jeans")
Man.dress_price(100)
Man.dress_size("l")
Man.display()
