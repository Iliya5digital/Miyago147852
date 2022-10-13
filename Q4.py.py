path='./Q4.txt'

def write():
    file.write('使用者輸入A')

def cut():
    x=int(input())
    length=len(file.read())
    file.truncate(length-x)

def move():
    x=int(input())
    file.seek(-x-1,2)
    tmp=file.readline()
    file.seek(1,0)
    file.write(tmp)
    length=len(file.read())
    file.truncate(length-x)

def point():
    file.seek(1,0)

def wq():
    for x in range(3):
        print('.')
    print('Saved!')
    print(file.read())

def switcher(keyin):
    d={
        'A': write,
        'B': cut,
        'C': move,
        'D': point,
        'E': wq
    }
    d.get(keyin)()

with open(path,'r+',encoding='utf8') as file:
    while True:
        s=input()
        switcher(s)
        if s=='E':
            break