# Python 3.5

def main():
    problem = open("A-test.txt", "r")
    output = open("A-out.txt", "w")

    test_case = int(problem.readline().strip())

    for test in range(test_case):
        line = problem.readline().strip().split()
        
        output.write("Case #" + str(test+1) + ": ")
        output.write(str(result) + "\n")
    problem.close()
    output.close()

main()
    
