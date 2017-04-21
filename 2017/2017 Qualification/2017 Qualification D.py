# Python 3.5

def rip_row_col(avail, row, col, N):
    for i in range(N):
        avail[i][col] = 0
        avail[row][i] = 0

def rip_diagonal(avail, row, col, N):
    if row > col:
        for i in range(N-row+col):
            avail[(row-col)+i][i] = 0
    else:
        for i in range(N-col+row):
            avail[i][(col-row)+i] = 0
    if row+col >= N:
        for i in range((row+col)-N+1, N):
            avail[i][(row+col)-i] = 0
    else:
        for i in range(row+col+1):
            avail[i][(row+col)-i] = 0

def main():
    problem = open("D-test.txt", "r")
    output = open("D-out.txt", "w")

    test_case = int(problem.readline().strip())

    for test in range(test_case):
        line = problem.readline().strip().split()
        N = int(line[0])
        M = int(line[1])
        stage = list()
        # 1 means available, 0 means not available
        plus_avail = list()
        x_avail = list()
        o_avail = list()
        for row in range(N):
            stage_row = list()
            plus_row = list()
            x_row = list()
            o_row = list()
            for col in range(N):
                stage_row.append('.')
                plus_row.append(1)
                x_row.append(1)
                o_row.append(1)
            stage.append(stage_row)
            plus_avail.append(plus_row)
            x_avail.append(x_row)
            o_avail.append(o_row)
        for model in range(M):
            line = problem.readline().strip().split()
            row = int(line[1]) - 1
            col = int(line[2]) - 1
            stage[row][col] = line[0]
            if line[0] == 'o':
                # x cannot be on same row/col
                rip_row_col(x_avail, row, col, N)
                rip_row_col(o_avail, row, col, N)
                # + cannot be on same diagonal
                rip_diagonal(plus_avail, row, col, N)
                rip_diagonal(o_avail, row, col, N)
        
        output.write("Case #" + str(test+1) + ": ")
    problem.close()
    output.close()

main()
    
