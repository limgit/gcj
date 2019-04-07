# Python 3.7.2

def main():
    test_case = int(input())
    for test in range(test_case):
        N = int(input())
        P = input()
        ans = "".join(["E" if ch == "S" else "S" for ch in P])
        print("Case #{}: {}".format(test+1, ans))


main()
