# Python 3.6.1

def main():
    test_case = int(input())
 
    for test in range(test_case):
        D, P = input().split()
        D = int(D)
        shoot_count = [0]
        total_dmg = 0
        for c in P:
            if c == 'C':
                shoot_count.append(0)
            if c == 'S':
                shoot_count[-1] += 1
                total_dmg += 2 ** (len(shoot_count) - 1)
        # For SCCSSC, shoot_count is [1, 0, 2, 0]
        # i.e. Number of Ss between each C
        hacks = 0
        top_non_zero_idx = len(shoot_count)-1
        while D < total_dmg:
            if top_non_zero_idx == 0:
                # We cannot reduce damage anymore
                break
            if shoot_count[top_non_zero_idx] == 0:
                top_non_zero_idx -= 1
                continue
            # Substitution with most damage reduce
            shoot_count[top_non_zero_idx] -= 1
            shoot_count[top_non_zero_idx-1] += 1
            total_dmg -= 2 ** (top_non_zero_idx - 1)
            hacks += 1
        if D >= total_dmg:
            print("Case #{}: {}".format(test+1, hacks))
        else:
            print("Case #{}: IMPOSSIBLE".format(test+1))
            

main()
    
