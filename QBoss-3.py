import random as rand
import time

n = 5
t = 0
genStr = ''


def gen():
    global genStr
    rd = [str(rand.randint(0, 9)) for i in range(n)]
    genStr = "".join(rd)
    return 0


def sub(Str):
    time.sleep(0.0001)
    ca = [0 for i in range(10)]
    num = [0 for i in range(10)]
    A = 0
    B = 0
    for i in range(n):
        ca[int(genStr[i])] += 1
    for i in range(n):
        if genStr[i] == Str[i]:
            A += 1
        num[int(Str[i])] += 1
    for i in range(10):
        if ca[i] < num[i]:
            B += ca[i]
        else:
            B += num[i]
    if A == n:
        timer()
        return '5A, over.'
    return str(A) + 'A' + str(B - A) + 'B'


def timer():
    global t
    st = time.perf_counter()
    if t == 1:
        t = 0
        ed = time.perf_counter()
        return (ed - st) * 1000
    t += 1


def main():
    gen()
    for i in range(10**n):
        mrd = [str(rand.randint(0, 9)) for i in range(n)]
        mStr = "".join(mrd)
        s = sub(mStr)
        print(s)
        if s == '5A, over.':
            print(mStr)
            break
    return 0


if __name__ == "__main__":
    timer()
    main()