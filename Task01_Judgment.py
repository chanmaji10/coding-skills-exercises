own = {}
own['x'], own['y'], own['height'], own['width']  = map(int, input().split())
n = int(input())
enemys = []
for _ in range(n):
    enemy = {}
    enemy['x'], enemy['y'], enemy['height'], enemy['width'] = map(int, input().split())
    enemys.append(enemy)

def judg(enemy):
    l = enemy['x'] + enemy['width'] < own['x'] 
    r = own['x'] + own['width'] < enemy['x']
    t = own['y'] > enemy['y'] + enemy['height']
    u = own['y'] + own['height'] < own['y']
    if True in [l,r,t,u]:
        return False
    else:
        return True
        
for i,enemy in enumerate(enemys):
    if judg(enemy):
        print('敵機{}が当たり'.format(i+1))
