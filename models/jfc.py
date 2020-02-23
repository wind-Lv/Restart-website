import sympy

def jfc(fc1,fc2):
    x,y = sympy.symbols("x y")
    a = sympy.solve([fc1,fc2],[x,y])
    return a

if __name__ == "__main__":
    fc1 = "3*x-2*y-3"
    fc2 = "x+2*y-5"
    print(jfc(fc1,fc2))