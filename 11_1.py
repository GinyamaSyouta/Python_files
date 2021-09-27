class Circle():
    PI = 3.1415 #円周率

    def __init__(self, r: int):
        self.r = r
    
    def calc_S(self):
        return (self.r ** 2) * self.PI

    def calc_F(self):
        return self.r * 2 * self.PI


class Main():

    def start(self):
        import math
        r1 = int(input("半径を整数値で入力："))
        Circle1 = Circle(r1)
        print("円周の長さは{}です".format(math.floor(Circle1.calc_F() * 1000) / 1000))
        print("円の面積は{}です".format(math.floor(Circle1.calc_S() * 1000) / 1000))

main = Main()
main.start()