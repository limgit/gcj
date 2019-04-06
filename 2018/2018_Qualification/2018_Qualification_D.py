# Python 3.6.1

import math

def rotate(point, a):
    x, y, z = point
    new_x = (math.cos(a) + 1/3 * (1 - math.cos(a))) * x\
          + (1/3 * (1 - math.cos(a)) - 1/math.sqrt(3) * math.sin(a)) * y\
          + (1/3 * (1 - math.cos(a)) + 1/math.sqrt(3) * math.sin(a)) * z
    new_y = (1/3 * (1 - math.cos(a)) + 1/math.sqrt(3) * math.sin(a)) * x\
          + (math.cos(a) + 1/3 * (1 - math.cos(a))) * y\
          + (1/3 * (1 - math.cos(a)) - 1/math.sqrt(3) * math.sin(a)) * z
    new_z = (1/3 * (1 - math.cos(a)) - 1/math.sqrt(3) * math.sin(a)) * x\
          + (1/3 * (1 - math.cos(a)) + 1/math.sqrt(3) * math.sin(a)) * y\
          + (math.cos(a) + 1/3 * (1 - math.cos(a))) * z
    return (new_x, new_y, new_z)

def plain(a):
    p = [0, 0, 0, 0, 0, 0]
    p[0] = rotate((0.5, 0.5, 0.5), a)
    p[1] = rotate((0.5, -0.5, 0.5), a)
    p[2] = rotate((0.5, -0.5, -0.5), a)
    p[3] = rotate((-0.5, -0.5, -0.5), a)
    p[4] = rotate((-0.5, 0.5, -0.5), a)
    p[5] = rotate((-0.5, 0.5, 0.5), a)
    new_p = []
    for x, y, z in p:
        new_p.append( (x, z) )
    area = 0
    for i in range(len(new_p)):
        x1, y1 = new_p[i]
        if i == len(new_p) - 1:
            x2, y2 = new_p[0]
        else:
            x2, y2 = new_p[i+1]
        area += (x1 * y2 - x2 * y1)
    return 1/2 * abs(area)

def main():
    T = int(input())

    for test in range(T):
        A = float(input())

        leftmost = 0
        rightmost = math.pi/3
        target = (leftmost + rightmost)/2
        area = plain(target)
        while abs(area - A) > 10**(-6):
            if area > A:
                rightmost = target
            else:
                leftmost = target
            target = (leftmost + rightmost)/2
            area = plain(target)
        print("Case #{}:".format(test+1))
        print( rotate((0.5, 0, 0), target) )
        print( rotate((0, 0.5, 0), target) )
        print( rotate((0, 0, 0.5), target) )

main()
