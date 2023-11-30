
def check_pw(pw):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if 'a' not in pw and 'e' not in pw and 'i' not in pw and 'o' not in pw and 'u' not in pw:
        return False
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1]:
            if pw[i] != 'e' and pw[i] != 'o':
                return False

        if i != len(pw)-2 and pw[i] in vowel and pw[i+1] in vowel and pw[i+2] in vowel:
            return False
        if i != len(pw)-2 and pw[i] not in vowel and pw[i+1] not in vowel and pw[i+2] not in vowel:
            return False
    return True

if __name__ == '__main__':
    while True:
        pw = input()
        if pw == 'end':
            break
        if check_pw(pw):
            print('<'+pw+'> is acceptable.')
        else:
            print('<'+pw+'> is not acceptable.')













