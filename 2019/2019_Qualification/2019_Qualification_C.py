# Python 3.7.3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def main():
    test_case = int(input())
    for test in range(test_case):
        N, L = [int(a) for a in input().split()]
        ciphertext = [int(a) for a in input().split()]
        p = gcd(ciphertext[0], ciphertext[1])
        plaintext = [ciphertext[0] // p]
        for cp in ciphertext:
            plaintext.append( cp // plaintext[-1] )
        decrypt_map = dict(zip(sorted(set(plaintext)), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        ans = "".join(map(lambda x: decrypt_map[x], plaintext))
        print("Case #{}: {}".format(test+1, ans))

main()
