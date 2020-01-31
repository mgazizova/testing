LANG_SYMBS = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

text = str(input()).split()
n = int(input())


def run(word):
    for shift in range(0, 26):
        out_text = encode(word, shift)

        if out_text is not None and out_text in text:
            print(out_text)
            break


def encode(word, shift):
    out = ''
    for char in word:
        is_decode = False
        for symbs in LANG_SYMBS:
            if char in symbs:
                index = (symbs.index(char) + shift) % len(symbs)
                out += symbs[index]
                is_decode = True
                if not isStartWith(out, text):
                    return None
        if not is_decode:
            out += char
    return out


def isStartWith(a, text):
    for el in text:
        if el.startswith(a):
            return True
    return False


for i in range(0, n):
    word = input()
    run(word)


