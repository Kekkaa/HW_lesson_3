import random

day = 20
month = 'апреля'
temperature = random.randint(-25, 35)

print(f'Сегодня {day} {month}. На улице {temperature} градусов.')

if temperature < 0:
    print('Холодно, лучше остаться дома')