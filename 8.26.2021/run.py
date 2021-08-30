import math

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x or self.y<other.y

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y-other.y)

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y+other.y)

    def __truediv__(self, f):
        return Coordinate(self.x/f, self.y/f)

    def __mul__(self, f):
        return Coordinate(self.x*f, self.y*f)

    def __repr__(self):
        return f"({self.x}, {self.y})"



def calc_x1(t):
    return Coordinate(50, t*15)

def calc_v2(x1, x2 , s):
    v = x2-x1
    return v*s / v.get_magnitude()
    

def calc_x2(v2, x2, step):
    return x2 + v2*step



def check_convergence(step, speed):
    t = 0
    x1 = Coordinate(50, 0)
    x2 = Coordinate(0, 0)
    v2 = Coordinate(15, 0)

    while x1.y < 100 and (x2 < x1):
        t += step
        x1 = calc_x1(t)
        x2 = calc_x2(v2, x2, step)
        v2 = calc_v2(x2, x1, speed)
        #print(x1, x2)

    return x1.y < 100
        


def run():
    low = 15
    high = 30
    step = 0.001


    for i in range(100):
        curr = .5*(high + low)
        converges = check_convergence(step, curr)
        if converges:
            high = curr
        else:
            low = curr

        print(curr, converges)


run()
