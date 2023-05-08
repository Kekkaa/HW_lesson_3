shoping_list = input('Введите названия продуктов: ').split()

print('\nСписок покупок: ')
for product in shoping_list:
    if len(product) % 2 == 0:
        print('-', product)