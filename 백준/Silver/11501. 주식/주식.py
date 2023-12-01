import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
  days = int(input().rstrip())
  prices = list(map(int, input().rstrip().split()))
  prices.reverse()
  answer = 0
  m = prices[0]

  for i in range(len(prices)):
    if prices[i] < m:
      answer += m - prices[i]
    else:
      m = prices[i]

  print(answer)
    
          
          