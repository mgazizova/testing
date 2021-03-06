# зашифровка
def encode(numbers, trans):
    # res = list()
    res = str()
    for el in numbers:
        index = trans.index(int(el))
        trans.pop(index)
        trans.insert(0, int(el))
        res += str(index+1) + ' '
        # res.append(index+1)
    return res


# расшифровка
def decode(numbers, trans):
    # res = list()
    res = str()
    for el in numbers:
        index = int(el)-1
        elem = trans[index]
        # res.append(elem)
        res += str(elem) + ' '
        trans.pop(index)
        trans.insert(0, elem)
    return res


while True:
    try:
        n, m, type = map(int, input().split())
        numbers = input().split()
        transposition = [i for i in range(1, m+1)]

        if type == 1:
            # зашифровать
            # encode_list = encode(numbers, transposition)
            # print(' '.join(map(str, encode_list)))
            print(encode(numbers, transposition))
        if type == 2:
            # расшифровать
            # decode_list = decode(numbers, transposition)
            # print(' '.join(map(str, decode_list)))
            print(decode(numbers, transposition))
    except Exception:
        pass