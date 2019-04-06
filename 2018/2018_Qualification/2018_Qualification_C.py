# Python 3.6.1
import sys

def main():
    T = int(input())

    for test in range(T):
        A = int(input())
        if A%9 == 0:
            test_cells = int(A/9)
        else:
            test_cells = int(A/9)+1

        end = False
        for idx in range(test_cells):
            matrix = [[0,0,0], [0,0,0], [0,0,0]]
            prepared = 0
            while prepared != 9:
                print (2 + 3*idx, 2)
                sys.stdout.flush()
                result = input().split()
                x = int(result[0])
                y = int(result[1])
                if x == 0 and y == 0:
                    end = True
                    break
                idx_x = x - 3*idx - 1
                idx_y = y - 1
                if matrix[idx_x][idx_y] == 0:
                    matrix[idx_x][idx_y] = 1
                    prepared += 1
            if end:
                break

main()
