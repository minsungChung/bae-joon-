
if __name__ == '__main__':
    def solution(n):

        i = 2

        while (i <= n):
            if n % i == 0:
                print(i)
                n //= i
            else:
                i += 1
        return

    n = int(input())

    solution(n)








