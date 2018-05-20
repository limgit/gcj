# Python 3.6.1

def main():
    test_case = int(input())
 
    for test in range(test_case):
        C = int(input())
        Bs = [int(a) for a in input().split()]
        if Bs[0] == 0 or Bs[-1] == 0:
            print("Case #{}: {}".format(test+1, "IMPOSSIBLE"))
        else:
            # Backtrace what happend through toy
            # We want to generate [1,1,1,...,1] finally
            loop = True
            Bs = [x-1 for x in Bs]
            rows = []  # Note that this has reversed order of rows
            while loop:
                loop = False
                ramps = []
                acc = 0
                for i in range(0, C):
                    if i == 0 or i == C-1:
                        ramps.append('.')
                    elif Bs[i] < 0:
                        loop = True
                        # We need to fill this hole
                        if acc > 0:
                            # The ball should come from left
                            Bs[i-1] -= 1
                            acc -= 1
                            Bs[i] += 1
                            # The ball in this slot is passed to left
                            ramps.append('/')
                        else:
                            # The ball should come from right
                            Bs[i+1] -= 1
                            Bs[i] += 1
                            # The ball in this slot is passed to right
                            ramps.append('\\')
                    else:
                        # We don't need to fill it
                        ramps.append('.')
                    acc += Bs[i]
                rows.append(ramps)
            print("Case #{}: {}".format(test+1, len(rows)))
            for row in rows:
                print(''.join(row)) 

main()
    
