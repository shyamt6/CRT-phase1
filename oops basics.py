class f15:
    def light(self):
        print("the light is on ")
    def fan(self,speed):
        print("THE fan is on ",speed)
        self.s=speed
    def cpu(self):
        print("on the system")
        print(self.s)

thanush=f15()
thanush.light()
thanush.fan(5)
thanush.cpu()