# Python 3.7.3
import sys

def modulo_inverse(a, m):
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r
    if r > 1:
        return "{} is not invertible".format(a)
    if t < 0:
        t += m
    return t


def main():
    T, N, M = [int(a) for a in input().split()]

    for test_case in range(T):
        remainders = {}
        dividers = [3, 4, 5, 7, 11, 13, 17]
        for divider in dividers:
            print(" ".join([str(divider)] * 18))
            sys.stdout.flush()
            result = [int(a) for a in input().split()]
            remainders[divider] = sum(result) % divider
        # We can use Chinese Remainder Theorem to find the number of gophers
        prod = 1021020 # Production of dividers
        x = 0
        for i in range(len(dividers)):
            nk = prod / dividers[i]
            sk = modulo_inverse(nk, dividers[i])
            x += remainders[dividers[i]] * nk * sk
        x = x % prod
        # Since 1021020 > 1000000, the answer is unique
        print(int(x))
        sys.stdout.flush()
        judge = int(input())
        if judge == -1:
            exit(1)


main()
