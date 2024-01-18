import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
pos = list(set(map(int, input().rstrip().split())))
pos.sort()
diff = [pos[i+1]-pos[i] for i in range(len(pos)-1)]
diff.sort(reverse=True)

print(sum(diff[K-1:]))
