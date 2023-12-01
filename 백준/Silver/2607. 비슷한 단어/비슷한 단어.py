
if __name__ == '__main__':

    n = int(input())
    word = list(input())
    answer = 0
    for _ in range(n-1):
        cnt = 1
        check = True
        word_copy = word[:]
        compare_word = list(input())
        for c in compare_word:
            if c in word_copy:
                word_copy.remove(c)
            else:
                if cnt == 1:
                    cnt -= 1
                else:
                    check = False
                    break
        if check and len(word_copy) < 2:
            answer += 1
            
    print(answer)









