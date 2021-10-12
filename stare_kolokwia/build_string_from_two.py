def possible(a, b, c):
    if len(a)+len(b) < len(c):
        return False
    letters = [0]*26
    for l in c:
        letters[ord(l)-ord('a')] -= 1
    for l in a:
        letters[ord(l)-ord('a')] += 1
    for l in b:
        letters[ord(l)-ord('a')] += 1
    for val in letters:
        if val < 0: return False
    return True


if __name__ == "__main__":
    u = "abcdef"
    v = "acefgh"
    w = "abcdefghz"
    print(possible(u, v, w))