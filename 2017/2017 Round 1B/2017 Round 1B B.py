# Python 3.5

def main():
    problem = open("B-test.txt", "r")
    output = open("B-out.txt", "w")

    T = int(problem.readline().strip())

    for test in range(T):
        
        output.write("Case #" + str(test+1) + ": ")
    problem.close()
    output.close()

main()
