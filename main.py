def perimetru():
    print('Perimetru dreptunghi')
    print("Introduceti prima latura a")
    a = input()
    print("Introduceti cea de a doua latura b")
    b = input()
    print("Introduceti cea de a treia latura c")
    c = input()
    print("Introduceti cea de a patra latura d")
    d = input()
    print("perimetrul dreptunghiului a + b + c + d = ", int(a)+int(b)+int(c)+int(d))

def arie():
    print("Arie dreptunghi")
    print("Introduceti lungimea L")
    L = input()
    print("Introduceti latimea l")
    l = input()
    print("Aria dreptunghiului L * l = ", int(L)*int(l))

def cerc():
    import math
    print(math.pi)
    print("Arie cerc")
    print("Introduceti raza cercului r")
    r = input()
    pi = input()
    print("Aria cercului pi * r^2 = ", int(pi)*int(r))



if __name__ == '__main__':
    perimetru()
    arie()
    cerc()