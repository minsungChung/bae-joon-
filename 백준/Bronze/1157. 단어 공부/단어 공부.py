

if __name__ == '__main__':

    word = input().upper()
    dict = {}
    for c in word:
        if c in dict.keys():
            dict[c] += 1
        else:
            dict[c] = 1

    largest = max(dict.values())
    answer = ''
    for key, value in dict.items():
        if value == largest and len(answer) == 0:
            answer += key
        elif value == largest and len(answer) > 0:
            answer = '?'
            break

    print(answer)







