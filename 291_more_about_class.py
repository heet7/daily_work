class mobile():

    def __init__(self,name,color):
        self.n = name
        self.c = color
        self.on = False
    
    def switch_on(self):
        self.on = True

mi = mobile('redmi','black')
# print(mi.n)
# print(mi.c)
# print(mi.on)

print(mi.on)
mobile.switch_on(mi)
print(mi.on)