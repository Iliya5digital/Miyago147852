import random as rand
import time

t = 0
genStr = ''


def gen():
    global genStr
    rd = [str(rand.randint(0, 10)) for i in range(5)]
    genStr = "".join(rd)
    return 0


def sub(Str):
    time.sleep(0.0001)
    if eval(genStr + '-' + Str) == 0:
        print(timer())


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
    for i in range(100000):
        sub(str(i))
    return 0


if __name__ == "__main__":
    timer()
    main()