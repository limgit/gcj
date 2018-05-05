# Python 3.6.1

def main():
    test_case = int(input())
 
    for test in range(test_case):
        N = int(input())
        Ws = [int(a) for a in input().split()]
        D = []
        C = []
        for _ in range(N):
            tmp1 = []
            tmp2 = []
            for _2 in range(N):
                tmp1.append(-1)
                tmp2.append(-1)
            D.append(tmp1)
            C.append(tmp2)
        for i in range(N):
            D[i][i] = Ws[i]
            C[i][i] = 1
        for length in range(2, N+1):
            for start in range(N-length+1):
                end = start + length - 1
                max_k = -1
                max_l = -1
                max_c = -1
                for k in range(start, end):
                    for l in range(k, end):
                    if D[k][l] <= 6 * Ws[end]:
                        if max_c < C[k][l]:
                            max_c = C[k][l]
                            max_k = k
                            max_l = l
                if max_k == -1:
                    D[start][end] = Ws[end]
                    C[start][end] = 1
                else: 
                    D[start][end] = D[max_k][max_l] + Ws[end]
                    C[start][end] = C[max_k][max_l] + 1
        print("Case #{}: {}".format(test+1, C[0][N-1]))
                
        
            

main()
    
