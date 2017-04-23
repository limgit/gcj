def main():
    problem = open("B-large-practice.in", "r")
    output = open("B-out.txt", "w")

    test = int(problem.readline().strip())

    for test_case in range(test):
        N = int(problem.readline().strip())
        soldiers = {}
        for i in range(2*N-1):
            line = problem.readline().strip().split()
            for elem in line:
                if elem in soldiers.keys():
                    soldiers[elem] += 1
                else:
                    soldiers[elem] = 1
        result = []
        for elem in soldiers.keys():
            if soldiers[elem] % 2 == 1:
                result.append(elem)
        result = sorted([int(a) for a in result])
        output.write("Case #" + str(test_case+1) + ": ")
        output.write(' '.join([str(a) for a in result]) + "\n")
    problem.close()
    output.close()

main()
