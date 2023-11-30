
if __name__ == '__main__':

    n, t_score, p = map(int, input().split())
    if n != 0:
        scores = list(map(int, input().split()))
        if n == p and scores[-1] >= t_score:
            print(-1)
        else:
            place = 1
            for score in scores:
                if t_score < score:
                    place+=1
            print(place)
    else:
        print(1)









