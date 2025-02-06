class Addition(object):
    def add(self, x,y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid Type: {} and {}".format(type(x), type(y)))

if __name__ == '__main__':
    calc = Addition()
    result = calc.add(2,2)
    print(f"Result of 2 + 2 = {result}")