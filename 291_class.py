class hourse(object):

    def __init__(self, color, price):
        self.color = color
        self.price = price


h = hourse(color='white', price='25l')
print(h.color)
h.price = 34524524
print(h.price)
print(h)

c = hourse('gray', 908789)
c.price = 45678909876
print("{}:{}\n\t{}:{}".format(h.color, h.price, c.color, c.price))
