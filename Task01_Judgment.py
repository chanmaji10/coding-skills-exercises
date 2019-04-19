own = {}
own['x'], own['y'], own['height'], own['width']  = map(int, input().split())
n = int(input())
enemys = []
for _ in range(n):
    enemy = {}
    enemy['x'], enemy['y'], enemy['height'], enemy['width'] = map(int, input().split())
    enemys.append(enemy)

def judg(enemy):
    if enemy['x'] > own['x'] + own['width']:
        if enemy['y'] > own['y'] + own['height']:
            return False
        elif enemy['y']+ enemy['height'] < own['y']:
            return False
        
    elif enemy['x'] + enemy['width'] < own['x']:
        if enemy['y'] > own['y'] + own['height']:
            return False
        elif enemy['y']+ enemy['height'] < own['y']:
            return False
    else:
        return True

for i,enemy in enumerate(enemys):
    if judg(enemy):
        print('敵機{}が当たり'.format(i+1))
