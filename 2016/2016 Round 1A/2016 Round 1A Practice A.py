def main():
    problem = open("A-large-practice.in", "r")
    output = open("A-out.txt", "w")

    test = int(problem.readline().strip())

    for test_case in range(test):
        S = problem.readline().strip()
        result = ''
        for idx in range(len(S)):
            if idx == 0:
                result += S[idx]
            elif result[0] > S[idx]:
                result += S[idx]
            else:
                result = S[idx] + result
        
        output.write("Case #" + str(test_case+1) + ": ")
        output.write(result + "\n")
    problem.close()
    output.close()

main()
