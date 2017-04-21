# Python 3.5

class Stop(Exception):
    pass

def main():
    problem = open("A-test.txt", "r")
    output = open("A-out.txt", "w")

    T = int(problem.readline().strip())

    for test in range(T):
        line = problem.readline().strip().split()
        R = int(line[0])
        C = int(line[1])
        grid = []
        for i in range(R):
            line = list(problem.readline().strip())
            grid.append(line)
        done = []
        for row in range(R):
            for col in range(C):
                if grid[row][col]!='?' and grid[row][col] not in done:
                    # Do sth
                    done.append(grid[row][col])
        output.write("Case #" + str(test+1) + ":" + "\n")
    problem.close()
    output.close()

def print_list(double_list):
    for e in double_list:
        print(e)

main()
