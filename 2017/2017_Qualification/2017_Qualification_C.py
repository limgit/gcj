# Python 3.5

import math

def main():
    problem = open("C-large.in", "r")
    output = open("C-out.txt", "w")

    test_case = int(problem.readline().strip())

    for test in range(test_case):
        line = problem.readline().strip().split()
        N = int(line[0])
        K = int(line[1])
        logK = int(math.log(K, 2))
        max_power_2 = 2 ** logK
        q = int((N - max_power_2 + 1)/max_power_2)
        r = (N - max_power_2 + 1) - q * max_power_2
        if (K - max_power_2) < r:
            selected_gap = q+1
        else:
            selected_gap = q
        if selected_gap % 2 == 0:
            max_lsrs = int(selected_gap/2)
            min_lsrs = max_lsrs - 1
        else:
            max_lsrs = int((selected_gap-1)/2)
            min_lsrs = max_lsrs
        output.write("Case #" + str(test+1) + ": " + str(max_lsrs) + " " + str(min_lsrs) + "\n")
    problem.close()
    output.close()

main()
    
