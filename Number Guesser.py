import random

print('Добро пожаловать в числовую угадайку')
print('Давайте решим в каком диапазоне будем угадывать')
diapazon = int(input('Введите число, в диапазоне которого вы хотите угадать число: '))


def is_valid(n):
    return n.isdigit() and int(n) in range(1, diapazon + 1)


def game_func():
    count = 0
    num = random.randint(1, diapazon)
    while True:
        print(f'Введите число от 1 до {diapazon}: ')
        n = input()
        if is_valid(n) is False:
            print(f'А может быть все-таки введем целое число от 1 до {diapazon}?')
            continue
        else:
            n = int(n)
            if n > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                count += 1
            elif n < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                count += 1
            else:
                count += 1
                print(f'Вы угадали за {count} попыток, поздравляем!')
                break


game_func()
while True:
    print('Хотите сыграть еще раз? (Да/Нет)')
    answer = input()
    if answer.lower() == 'да' or answer.lower() == "д" or answer.lower() == 'yes':
        game_func()
    elif answer.lower() == 'нет' or answer.lower() == "н" or answer.lower() == 'no':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
    else:
        print('Простите, я вас не понял, так вы хотите поиграть?')
