# Python 3.7.2

def main():
    test_case = int(input())
    for test in range(test_case):
        N = int(input())
        A = N
        B = 0
        pos = 1
        while N > 0:
            digit = N % 10
            if digit == 4:
                A -= pos
                B += pos
            N //= 10
            pos *= 10
        print("Case #{}: {} {}".format(test+1, A, B))

main()
