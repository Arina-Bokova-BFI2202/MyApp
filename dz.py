a, b, c = [float(i) for i in input().split()]
d = (b**2-4*a*c)
if d >= 0:
    x1 = (-b + d**0.5)/2*a
    x2 = (-b - d**0.5)/2*a
    if x1==x2:
        print(x1)
    else:
        print(x1, x2)
else:
    print('Корней нет')