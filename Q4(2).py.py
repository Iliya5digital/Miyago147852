import io

text=''
write='使用者輸入A'
pt=0
path='./Q4.txt'

def write(s):
    global text, pt
    text_list=list(text)
    text_list.insert(pt, s)
    text = ''.join(text_list)
    pt+=len(s)-1

def cut():
    global text, pt
    x=input()
    text=text[:len(text)-x]
    pt-=x
    #text='testtext'
def move():
    tmp=text[len(text)+1-input():]
    write(tmp)

def point():
    global pt
    pt=0

def wq():
    with open(path,'r+',encoding='utf8') as file:
        file.write(text)
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
    return d.get(keyin)

while True:
    o=input()
    switcher(o)(write)
    if o=='E':
        break