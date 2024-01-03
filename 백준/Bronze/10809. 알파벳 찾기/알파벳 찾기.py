
def find_alphabet(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dict = {a: -1 for a in alphabet}
    for i, v in enumerate(s):
        if dict[v] == -1:
            dict[v] = i

    for a in alphabet:
        print(dict[a], end=' ')

if __name__ == '__main__':
    find_alphabet(input())



