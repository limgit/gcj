# Python 3.6.1
import sys

def main():
    test_case = int(input())
 
    for test in range(test_case):
        N = int(input())
        stock = []
        pref = []
        for _ in range(N):
            stock.append(1)
            pref.append(0)
        for _ in range(N):
            l = [int(a) for a in input().split()]
            D = l[0]
            likes = l[1:]
            for candy in likes:
                pref[candy] += 1
            if D == 0:
                # We cannot sell the lollipop
                print(-1)
                sys.stdout.flush()
            elif D == 1:
                if stock[likes[0]] != 0:
                    # We can sell
                    stock[likes[0]] -= 1
                    print(likes[0])
                    sys.stdout.flush()
                else:
                    # We cannot sell
                    print(-1)
                    sys.stdout.flush()
            else:
                # find the candy with lowest probability
                # according to the observation until now
                avail_likes_with_pref = []
                for candy in likes:
                    if stock[candy] != 0:
                        # Get candies with preference
                        # which have available stocks
                        avail_likes_with_pref.append( (pref[candy], candy) )
                if len(avail_likes_with_pref) == 0:
                    # We do not have stock for any candies customer likes
                    # so, we cannot sell
                    print(-1)
                    sys.stdout.flush()
                else:
                    # Get the candy with lowest preference
                    avail_likes_with_pref.sort()
                    sell = avail_likes_with_pref[0][1]
                    # Sell it
                    stock[sell] -= 1
                    print(sell)
                    sys.stdout.flush()
                
main()
    
