import sys

str_suits = ['S', 'C', 'D', 'H']
str_numbers = ['0','A'] + [str(i) for i in range(2,11)] + ['J', 'Q', 'K']
cards = [list(map(int, input().split())) for i in range(5)]
cards = sorted(cards, key=lambda x: x[1])
suits = list(map(lambda x: x[0], cards))
numbers = list(map(lambda x: x[1], cards))
u_nums = set(numbers)
u_num_cnt = [numbers.count(u_num) for u_num in u_nums]

def onePea():
    if len(u_nums) == 4:
        return True
        
def twoPea():
    if u_num_cnt.count(2) == 2:
        return True

def threeCards():
    if max(u_num_cnt) == 3:
        return True

def fourCards():
    if max(u_num_cnt) == 4:
        return True
    
def straight():
    straight_patterns = [[1, 10, 11, 12, 13], [1, 2, 11, 12, 13], [1, 2, 3, 12, 13], [1, 2, 3, 4, 13]]
    if True in [numbers==s_pattern for s_pattern in straight_patterns]:
        return True
    elif len(u_nums) == 5 and numbers[0]+4 == numbers[4]:
        return True
        
def flash():
    if len(set(suits)) == 1:
        return True
        
def fullHouse():
    if len(u_nums) == 2 and max(u_num_cnt) == 3:
        return True  
        
def straightFlash():
    if flash() == straight() == True:
        return True
        
def royalFlash():
    if flash()  and numbers == [1, 10, 11, 12, 13]:
        return True

def out(hand):
    print(' '.join([str_suits[s]+str_numbers[n] for s,n in zip(suits, numbers)]))
    print(hand)
    sys.exit()

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
