import random

print('Добро пожаловать в числовую угадайку.')
print('Опишу суть игры.')
print('В начале игры компьютер загадывает случайное число в диапазоне от 1 до 100 включительно.')
print('Ваша задача отгадать число, которое загадал компьютер. Приступим!')

num = random.randint(1, 100)


def is_valid(a):
    if a.isdigit() and 1 <= int(a) <= 100:
        return True


print('Введите число от 1 до 100:')


def is_valid_input():
    while True:
        answer = input()
        if is_valid(answer):
            return int(answer)
        if not is_valid(answer):
            print("Нет нет нет, нужно ввести целое число от 1 до 100. Буквы, слова, фразы и знаки препинания не принимаются.")


def compare_num():
    global num
    times = 0
    while True:
        ans = is_valid_input()
        if ans < num:
            times += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif ans > num:
            times += 1
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif ans == num:
            times += 1
            print("Поздравляем, вы угадали! Количество попыток:", times)
            if times > 7:
                print('Расскажу один секрет. Для угадывания числа из данного диапазона достаточно 7 попыток. Спросите как?')
                print('Всё очень просто! Для этого достаточно на каждом шаге брать среднее значение полученного диапазона.')
                print('Таким образом диапазон угадывания после каждого шага будет сокращаться в 2 раза.')
                print('В следующей игре предлагаю в первой попытке начать со значения 50.')
                print("Хотите убедиться в этом?:) (Да/Нет)")
                ans2 = input()
                if "да" in ans2.lower() or "yes" in ans2.lower() or '+' in ans2.lower() or 'давай' in ans2.lower():
                    num = random.randint(1, 100)
                    print('Правила те же: введите число от 1 до 100.')
                    compare_num()
                elif ans2.lower() == "нет" or ans2.lower() == 'ytn' or ans2.lower() == 'no' or ans2.lower() == '-':
                    print('Спасибо за игру! Еще увидимся;)')
            else:
                print('Хотите сыграть еще раз?:)')
                ans3 = input()
                if "да" in ans3.lower() or "yes" in ans3.lower() or '+' in ans3.lower() or 'давай' in ans3.lower():
                    num = random.randint(1, 100)
                    print('Правила те же: введите число от 1 до 100.')
                    compare_num()
                elif ans3.lower() == "нет" or ans3.lower() == 'ytn' or ans3.lower() == 'no' or ans3.lower() == '-':
                    print('Спасибо за игру! Еще увидимся;)')


compare_num()
input()