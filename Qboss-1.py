import random as rand
import time

t = 0
genStr = ''


def gen():
    global genStr
    rd = [str(rand.randint(0, 10)) for i in range(4)]
    genStr = "".join(rd)
    return 0


def sub(Str):
    if eval(genStr + '-' + Str) == 0:
        print(timer())
        return 0
    return str(eval(genStr + '-' + Str))


def timer():
    global t
    st = time.perf_counter()
    if t == 1:
        ed = time.perf_counter()
        return (ed - st) * 1000
    t += 1


def main():
    gen()
    rdM = [str(rand.randint(0, 10)) for i in range(4)]
    mainStr = "".join(rdM)
    sub(str(eval(mainStr + "+" + sub(mainStr))))
    return 0


if __name__ == "__main__":
    timer()
    main()