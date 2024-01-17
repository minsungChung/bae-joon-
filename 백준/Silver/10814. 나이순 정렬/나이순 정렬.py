import sys
input = sys.stdin.readline

n = int(input().rstrip())
members = []

for _ in range(n):
    member = list(input().rstrip(). split())
    member[0] = int(member[0])
    members.append(member)

members.sort(key=lambda x:x[0])

for mem in members:
    print(mem[0], mem[1])