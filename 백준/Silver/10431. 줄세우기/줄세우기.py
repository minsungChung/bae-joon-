
p = int(input())

for j in range(1, p+1):

    t_list = list(map(int, input().split()))
    t = t_list.pop(0)
    sorted_list = []
    cnt = 0

    for num in t_list:
        sorted_list.append(num)
        for i in range(len(sorted_list)-1, 0, -1):
            if sorted_list[i-1] > sorted_list[i]:
                tmp = sorted_list[i-1]
                sorted_list[i-1] = sorted_list[i]
                sorted_list[i] = tmp
                cnt += 1
            else:
                break

    print(j, cnt)

