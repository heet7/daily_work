class mobile():
    # kind of static method
    factory = 'Gujrat'  # class attribute

    def __init__(self, n, p):
        self.name = n
        self.price = p
        self.on = False

    def switch_on(self):
        self.on = True


mi = mobile('note 7 pro', 14500)
mobile.switch_on(mi)
mi.power = 2044
# print(mi.power)
print()

mi.factory = "london"
print("factory of mi in",mi.factory)
print()

samsung = mobile('note 10', 95632)
print("factory of samsung in",samsung.factory)
print()

print('values in mi')
for key, val in mi.__dict__.items():
    print(f'{key} '+chr(9)+f': {val}')

print()

print('values in samsung')
for key, val in samsung.__dict__.items():
    print(f'{key} '+chr(9)+f': {val}')


print(mi.factory)
print(samsung.factory)
