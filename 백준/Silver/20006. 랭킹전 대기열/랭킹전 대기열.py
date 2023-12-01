import sys

def print_playsers(lst, startorwait):
  print(startorwait)
  lst.sort(key=lambda x:x[1])
  for l, n in lst:
    print(l, n)

input = sys.stdin.readline
# p는 플레이어의 수, m은 방의 정원
p, m = map(int, input().rstrip().split())
room = []
for _ in range(p):
  level, player = input().rstrip().split()
  if len(room) == 0:
    room.append([[int(level), player]])
  else:
    c = True
    for i in range(len(room)):
      if room[i][0][0] - int(level) >= -10 and room[i][0][0] - int(level) <= 10 and len(room[i]) < m:
        c = False
        room[i].append([int(level), player])
        break
    if c:
      room.append([[int(level), player]])

for r in room:
  if len(r) < m:
    print_playsers(r, 'Waiting!')
  else:
    print_playsers(r, 'Started!')
          
          