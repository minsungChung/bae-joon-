a, b = map(int, input().split())

if a > b:
    big = a
    small = b
else :
    big = b
    small = a

r = big % small

while r != 0:
    big = small
    small = r
    r = big % small
print(small)
print(a * (b//small))