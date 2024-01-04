import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input().rstrip())
    a = set(map(int, input().rstrip().split()))
    m = int(input().rstrip())
    nums = list(map(int, input().rstrip().split()))

    for num in nums:
        print(1 if num in a else 0)





