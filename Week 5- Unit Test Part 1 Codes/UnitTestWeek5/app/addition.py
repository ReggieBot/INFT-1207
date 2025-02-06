class Addition(object):
    def add(self, x,y):
        return x + y

if __name__ == '__main__':
    calc = Addition()
    result = calc.add(2,2)
    print(f"Result of 2 + 2 = {result}")