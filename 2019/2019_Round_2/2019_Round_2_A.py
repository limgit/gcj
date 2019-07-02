def main():
    T = int(input())
    for test in range(T):
        N = int(input())
        molecules = []
        for _ in range(N):
            x = [int(a) for a in input().strip().split()]
            molecules.append(tuple(x))
        slope_set = set()
        for i in range(N-1):
            for j in range(i+1, N):
                mol1 = molecules[i]
                mol2 = molecules[j]
                slope_sign = (mol1[0] - mol2[0]) * (mol1[1] - mol2[1])
                if slope_sign < 0:
                    slope = (mol1[0] - mol2[0]) / (mol1[1] - mol2[1])
                    slope_set.add(slope)
        print("Case #{}: {}".format(test+1, len(slope_set)+1))


main()