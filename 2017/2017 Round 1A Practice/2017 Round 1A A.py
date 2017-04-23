def fill_the_cake(cake, row_t, row_b, col_l, col_r):
    num_alphabet = 0
    top_alphabet = ''
    topmost_row = 0
    botmost_row = 0
    leftmost_col = col_r
    for row in range(row_t, row_b):
        for col in range(col_l, col_r):
            if cake[row][col] != '?':
                if num_alphabet == 0:
                    topmost_row = row
                    top_alphabet = cake[row][col]
                botmost_row = row
                if leftmost_col > col:
                    leftmost_col = col
                num_alphabet += 1
    if num_alphabet == 1: # Only alphabet
        for row in range(row_t, row_b):
            for col in range(col_l, col_r):
                cake[row][col] = top_alphabet
    elif topmost_row == botmost_row: # Divide by column
        fill_the_cake(cake, row_t, row_b, col_l, leftmost_col + 1)
        if leftmost_col + 1 < col_r:
            fill_the_cake(cake, row_t, row_b, leftmost_col + 1, col_r)
    else: # Divide by row
        fill_the_cake(cake, row_t, topmost_row + 1, col_l, col_r)
        if topmost_row + 1 < row_b:
            fill_the_cake(cake, topmost_row + 1, row_b, col_l, col_r)

def main():
    problem = open("A-large-practice.in", "r")
    output = open("A-out.txt", "w")

    test = int(problem.readline().strip())

    for test_case in range(test):
        line = problem.readline().strip().split()
        R = int(line[0])
        C = int(line[1])
        cake = []
        for row in range(R):
            cake.append( list(problem.readline().strip()) )
        fill_the_cake(cake, 0, R, 0, C)
        output.write("Case #" + str(test_case+1) + ":\n")
        for i in range(R):
            output.write(''.join(cake[i]) + '\n')
    problem.close()
    output.close()

    
main()
