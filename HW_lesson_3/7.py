#Последовательность Фибоначчи (порядок, значение)
# 1 2 3 4 5 6 7  8  9  10 11 12
# 1 1 2 3 5 8 13 21 34 55 89 144

n = -1
while n < 10:
    n = int(input('Введите положительное число: '))

f_numb = [1, 1]

if n == 1 or n == 2:
    print(f'На {n} позиции последовательности Фиббоначи стоит число {f_numb[0]}')
elif n > 2:
    for i in range(2, n):
        f_numb.append(f_numb[i-1] + f_numb[i-2])
    print(f'На {n} позиции последовательности Фиббоначи стоит число', f_numb[n-1])