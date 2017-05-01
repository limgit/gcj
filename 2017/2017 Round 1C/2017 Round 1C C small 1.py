# Python 3.6.1

def main():
    problem = open("C-small-1-attempt1.in", "r")
    output = open("C-out.txt", "w")

    T = int(problem.readline().strip())

    for test in range(T):
        line = problem.readline().strip().split()
        N = int(line[0])
        K = int(line[1])
        U = float(problem.readline().strip())
        P = [float(x) for x in problem.readline().strip().split()]

        # Use AM-GM inequality
        maximum = ((sum(P) + U) / N) ** N
        output.write("Case #" + str(test+1) + ": ")
        output.write(str(round(maximum, 6)) + "\n")
    problem.close()
    output.close()

main()
