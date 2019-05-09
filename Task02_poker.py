import sys

def fourCards():
    if len(set(numbers)) == 2:
        n = list(set(numbers))
        if max(numbers.count(n[0]), numbers.count(n[1])) == 4:
            return True
        
def fullHouse():
    if len(set(numbers)) == 2:
        n = list(set(numbers))
        if max(numbers.count(n[0]), numbers.count(n[1])) == 3:
            return True    

def flash():
    if len(set(suits)) == 1:
        return True

def straight():
    if True in [n==numbers for n in [[1, 10, 11, 12, 13], [1, 2, 11, 12, 13], [1, 2, 3, 12, 13], [1, 2, 3, 4, 13]]]:
        return True
    elif len(set(numbers)) == 5 and numbers[0]+4 == numbers[4]:
        return True

def threeCards():
    if len(set(numbers)) < 4:
        n = list(set(numbers))
        n_cnt = [numbers.count(n_i) for n_i in n]
        if max(n_cnt) == 3:
            return True
        
def twoPea():
    if len(set(numbers)) == 3:
        n = list(set(numbers))
        n_cnt = [numbers.count(n_i) for n_i in n]
        if n_cnt.count(2) == 2:
            return True

def onePea():
    if len(set(numbers)) == 4:
        return True
    
def royalFlash():
    if len(set(suits)) == 1 and numbers == [1, 10, 11, 12, 13]:
        return True

def straightFlash():
    if flash() == straight() == True:
        return True
    
def out(hand):
    print(' '.join([str_suits[s]+str_numbers[n] for s,n in zip(suits, numbers)]))
    print(hand)
    sys.exit()

str_suits = ['S', 'C', 'D', 'H']
str_numbers = ['0','A'] + [str(i) for i in range(2,11)] + ['J', 'Q', 'K']
cards = [list(map(int, input().split())) for i in range(5)]
cards = sorted(cards, key=lambda x: x[1])
suits = list(map(lambda x: x[0], cards))
numbers = list(map(lambda x: x[1], cards))

out('ロイヤルフラッシュ') if royalFlash() else None
out('ストレートフラッシュ') if straightFlash() else None
out('フォーカード') if fourCards() else None
out('フルハウス') if fullHouse() else None
out('フラッシュ') if flash() else None
out('ストレート') if straight() else None
out('スリーカード') if threeCards() else None
out('ツーペア') if twoPea() else None
out('ワンペア') if onePea() else None
out('ハイカード')