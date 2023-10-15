
if __name__ == '__main__':
    def solution(n, m):
        visited = [0] * (m+1)
        for i in range(2, int(m**(1/2))+1):
            j = 2
            while i*j <= m:
                if visited[i*j] == 0:
                    visited[i*j] = 1
                j += 1

        for i in range(n, m+1):
            if visited[i] == 0 and i != 1:
                print(i)


    n, m = map(int, input().split())

    solution(n, m)








