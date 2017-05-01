# Python 3.6.1

def main():
    problem = open("B-test.txt", "r")
    output = open("B-out.txt", "w")

    T = int(problem.readline().strip())

    for test in range(T):
        line = problem.readline().strip().split()
        AC = int(line[0])
        AJ = int(line[1])
        AC_list = []
        AJ_list = []
        for i in range(AC):
            line = problem.readline().strip().split()
            AC_list.append( tuple(int(a) for a in line) )
        for i in range(AJ):
            line = problem.readline().strip().split()
            AJ_list.append( tuple(int(a) for a in line) )
        AC_list.sort()
        AJ_list.sort()
        exchange += 2 * min(len(new_list[0]), len(new_list[1]))
        output.write("Case #" + str(test+1) + ": ")
        output.write(str(exchange) + "\n")
    problem.close()
    output.close()

main()
