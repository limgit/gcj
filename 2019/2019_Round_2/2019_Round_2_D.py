def main():
    T = int(input())
    for test in range(T):
        M = int(input())
        formula = []
        for _ in range(M):
            x = tuple(int(a)-1 for a in input().strip().split())
            formula.append(x)
        metals = [int(a) for a in input().strip().split()]
        initial = metals[:]
        formula_used = [False] * M
        def is_all_formula_used():
            ret = True
            for i in range(M):
                if metals[i] != 0 and not formula_used[i]:
                    ret = False
            return ret
        while not is_all_formula_used():
            for i in range(M):
                if metals[i] != 0 and not formula_used[i]:
                    use = formula[i]
                    coef = metals[i]
                    metals[use[0]] += coef
                    metals[use[1]] += coef
                    metals[i] -= coef
                    formula_used[i] = True
                    break

main()