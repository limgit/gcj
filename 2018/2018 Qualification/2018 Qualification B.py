# Python 3.6.1

import sys

def main():
    T = int(input())

    for test in range(T):
        N = int(input())

        # Surprisingly Trouble Sort sorts the sublist of the list
        # : the sublist of odd poisitioned elements and
        # the sublist of even poisitioned elements.
        # Therefore, sort sublists seperately and check if the full list
        # is sorted
        V = [int(a) for a in input().split()]
        even_V = [int(V[i]) for i in range(len(V)) if i % 2 == 0] # O(N)
        odd_V = [int(V[i]) for i in range(len(V)) if i % 2 == 1] # O(N)
        even_V.sort() # O(N log N)
        odd_V.sort() # O(N log N)
        may_sorted_V = []
        for i in range(len(V)): # O(N)
            if i % 2 == 0:
                may_sorted_V.append(even_V[i//2])
            else:
                may_sorted_V.append(odd_V[(i-1)//2])
        problem_idx = -1
        for i in range(len(V)-1):
            if may_sorted_V[i] > may_sorted_V[i+1]:
                problem_idx = i
                break
        if problem_idx == -1:
            print("Case #{}: OK".format(test+1))
        else:
            print("Case #{}: {}".format(test+1, problem_idx))
        
        
main()
