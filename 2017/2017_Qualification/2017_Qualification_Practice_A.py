def main():
    problem = open("A-large-practice.in", "r")
    output = open("A-out.txt", "w")

    test = int(problem.readline().strip())

    for test_case in range(test):
        line = problem.readline().strip().split()
        S = list(line[0])
        K = int(line[1])
        flip = 0
        for i in range(len(S)-K+1):
            if S[i] == '-':
                flip += 1
                for j in range(i, i+K):
                    if S[j] == '-': S[j] = '+'
                    else: S[j] = '-'
        impossible = False
        for i in range(len(S)-K+1, len(S)):
            if S[i] == '-':
                impossible = True
        output.write("Case #" + str(test_case+1) + ": ")
        if impossible:
            output.write("IMPOSSIBLE\n")
        else:
            output.write(str(flip) + "\n")
    problem.close()
    output.close()

main()
