
if __name__ == '__main__':

    n, game = input().split()
    l = [input() for _ in range(int(n))]
    s = set(l)

    if game == 'Y':
        print(len(s))
    elif game == 'F':
        print(len(s)//2)
    elif game == 'O':
        print(len(s)//3)











