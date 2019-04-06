# Python 3.6.1

from functools import reduce

def main():
    test_case = int(input())
 
    for test in range(test_case):
        N, L = tuple([int(a) for a in input().split()])
        pos_letters = []
        words = []
        for _ in range(L):
            pos_letters.append([])
        for _ in range(N):
            word = input()
            words.append(word)
            for i in range(len(word)):
                char = word[i]
                if char not in pos_letters[i]:
                    pos_letters[i].append(char)
        pos_letters_count = list(map(len, pos_letters))
        total_avail = reduce(lambda x,y: x*y, pos_letters_count, 1)
        for elem in pos_letters:
            elem.sort()
        if N == total_avail:
            # There can be no more words
            print("Case #{}: -".format(test+1))
        else:
            words_id = []
            for word in words:
                word_id = 0
                for i in range(len(word)):
                    word_id *= pos_letters_count[i]
                    word_id += pos_letters[i].index(word[i])
                words_id.append(word_id)
            words_id.sort()
            broke = False
            if words_id[0] != 0:
                target_word_id = 0
                broke = True
            else: 
                for i in range(len(words_id)-1):
                    if words_id[i] + 1 != words_id[i+1]:
                        target_word_id = words_id[i]+1
                        broke = True
                        break
            if not broke:
                target_word_id = words_id[-1]+1
            target_word = ''
            for i in range(len(pos_letters_count)-1, -1, -1):
                idx = target_word_id % pos_letters_count[i]
                target_word = pos_letters[i][idx] + target_word
                target_word_id //= pos_letters_count[i]
            print("Case #{}: {}".format(test+1, target_word))
            

main()
    
