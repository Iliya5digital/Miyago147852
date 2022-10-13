import random as rand

Cards=[]
cards=[]
suit=[0 for i in range(4)]
symbol=[0 for i in range(13)]
suits=["Shades","Hearts","Diamonds","Clubs"]
symbols=[str(i+1) for i in range(13)]
symbols[0]='A'
symbols[10]='J'
symbols[11]='Q'
symbols[12]='K'
card=[i for i in range(52)]

rand.shuffle(card)

for i in range(5):
    suit[card[i]//13]+=1
    symbol[card[i]%13]+=1
    cards.append(suits[card[i]//13])
    cards.append(symbols[card[i]%13])
    Cards.append(' '.join(cards))
    cards=[]

def Check():
    flush=0
    straight=0
    A_straight=0
    four_of_a_kind=0
    three_of_a_kind=0
    pair=0
    count=0
    for i in range(4):
        if suit[i]==5:
            flush=1
    for i in range(13):
        if symbol[i] != 0:
            end = i;
            if symbol[i]==4:
                four_of_a_kind=1
            elif symbol[i]==3:
                three_of_a_kind=1
            elif symbol[i]==2:
                pair+=1
            elif symbol[i] == 1:
                count+=1
    if count==5:
        if symbol[0] and symbol[9] and symbol[10] and symbol[11] and symbol[12]:
            a_straight=1
        else:
            start=end-count+1
            for i in range(start,end):
                if symbol[i]:
                    count-=1
            if count==0:
                straight=1
    if A_straight and flush:
        return "Royal Straight Flush!!!"
    elif straight and flush:
        return "Straight Flush!"
    elif four_of_a_kind:
        return "Four of a kind!"
    elif three_of_a_kind and pair:
        return "Full House!"
    elif flush==1:
        return "Flush!"
    elif straight or A_straight:
        return "Straight!"
    elif three_of_a_kind:
        return "Three of a kind!"
    elif pair:
        return "Pair!"
    else:
        return "Separate..."

print("Result:",Cards)
print("Type:",Check())