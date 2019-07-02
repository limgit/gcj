
def main():
    T = int(input())
    for test in range(T):
        N = int(input())
        molecules = []
        for _ in range(N):
            x = tuple(int(a) for a in input().strip().split())
            molecules.append(x)
        impossible = False
        target_diff = None
        for i in range(N-1):
            mol1 = molecules[i]
            mol2 = molecules[i+1]
            diff = (mol2[0] - mol1[0], mol2[1] - mol1[1])
            if diff[0] <= 0 and diff[1] <= 0:
                impossible = True
                break
            elif diff[0] >= 0 and diff[1] >= 0:
                continue
            else:
                if target_diff is None:
                    target_diff = diff
                else:
                    if target_diff[0] * diff[0] < 0:
                        impossible = True
                        break
                    else:
                        if diff[0] > 0:
                            curr_c = -diff[1] / diff[0]
                            target_c = -target_diff[1] / target_diff[0]
                            if curr_c < target_c:
                                target_diff = diff
                        else:
                            curr_j = -diff[0] / diff[1]
                            target_j = -target_diff[0] / target_diff[1]
                            if curr_j < target_j:
                                target_diff = diff
        if impossible:
            print("Case #{}: IMPOSSIBLE".format(test+1))
        else:
            if target_diff is None:
                print("Case #{}: 1 1".format(test+1))
            else:
                if target_diff[0] > 0:
                    print("Case #{}: {} 1".format(test+1, -target_diff[1] // target_diff[0] + 1))
                else:
                    print("Case #{}: 1 {}".format(test+1, -target_diff[0] // target_diff[1] + 1))

main()