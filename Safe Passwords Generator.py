import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
chars_1 = ''
cntPw = input('Укажите количество паролей для генерации: ')
lenPw = input('Укажите длину одного пароля: ')
digOn = input('Включать ли цифры 0123456789? (y/n): ')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n): ')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n): ')
if digOn.lower() == 'y':
    chars += digits
if ABCon.lower() == 'y':
    chars += uppercase_letters
if abcOn.lower() == 'y':
    chars += lowercase_letters
if chOn.lower() == 'y':
    chars += punctuation
if excOn.lower() == 'y':
    for i in range(len(chars)):
        if chars[i] not in 'il1Lo0O':
            chars_1 += chars[i]
        else:
            continue
if excOn.lower() == 'n':
    chars_1 = chars


def generate_password(lenPw, chars_1):
    password = ''
    for j in range(int(lenPw)):
        password += random.choice(chars_1)
    return password


for i in range(int(cntPw)):
    print('Мы сгенерировали для вас следующие пароли:',generate_password(lenPw, chars_1))
