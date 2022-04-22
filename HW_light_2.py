num_5 = 0
for i in range(10):
    num = int(input("Введите произвольную цифру: "))
    if num == 5:
        num_5 += 1

print(f'Количество введенных пользователем цифр 5: {num_5}')