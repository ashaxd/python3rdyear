import itertools,random
deck=list(itertools.product(range(1,14),['spade','heat','diamond','clb']))
random.shuffle(deck)
for i in range(5):
    print(deck[i][0],"of",deck[i][1])