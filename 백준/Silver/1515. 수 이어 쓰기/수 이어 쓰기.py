
if __name__ == '__main__':
    nums = input()
    i = 0
    curr = 0
    largest = 0
    while True:
        if curr == len(nums):
            print(largest)
            break
        i += 1
        for c in str(i):
            if curr == len(nums):
                break

            if nums[curr] == c:
                largest = i
                curr += 1












