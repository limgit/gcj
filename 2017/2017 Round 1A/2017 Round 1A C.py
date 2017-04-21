# Python 3.5

def main():
    problem = open("C-test.txt", "r")
    output = open("C-out.txt", "w")

    T = int(problem.readline().strip())

    for test in range(T):
        line = problem.readline().strip().split()
        Hd = int(line[0])
        Ad = int(line[1])
        Hk = int(line[2])
        Ak = int(line[3])
        B = int(line[4])
        D = int(line[5])
        
        output.write("Case #" + str(test+1) + ":")
    problem.close()
    output.close()

main()
