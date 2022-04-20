'''
Calculator of russians losses in a war with Ukraine.

====================================================
'''


import os, pathlib, time


file_loss = os.path.join(os.path.dirname(__file__), 'old_losses.txt')
file_path = pathlib.Path(file_loss)
beginning = f'''+{'-' * 94}+
|{' ' * ((94-26)//2)}СВИНОСОБАЧІ ВТРАТИ ЗА ДОБУ{' ' * ((94-26)//2)}|
+{'=' * 94}+'''
end = f'''+{'=' * 94}+
|{' ' * ((94-58)//2)}СЛАВА УКРАЇНІ, СЛАВА НАЦІЇ І ПІЗДЕЦЬ РОСІЙСЬКІЙ ФЕДЕРАЦІЇ!{' ' * ((94-58)//2)}|
|{' ' * ((94-40)//2)}.. БОРІТЕСЯ -- ПОБОРЕТЕ ВАМ БОГ ПОМАГАЄ!{' ' * ((94-40)//2)}|
|{' ' * ((94-42)//2)}ЗА ВАС ПРАВДА, ЗА ВАС СЛАВА І ВОЛЯ СВЯТАЯ!{' ' * ((94-42)//2)}|
+{'-' * 94}+'''

new_losses = {
    'Добрива для нашої землі(Вбиті окупанти)': 0,
    'Металобрухт(Знищені танки)': 0,
    'Консервна бляшанка(Знищені БТР)': 0,
    'Гівно-рогатки(Знищені Арт-Системи)': 0,
    'Гівномети(Знищені РСЗВ)': 0,
    'Те що заляпує гівном наші ракети (Знищені ППО)': 0,
    'Літальний металобрухт (Знищені літаки)': 0,
    'Літальні консервні бляшанки (Знищені гелікоптери)': 0,
    'Літальні пляшки з фотоапаратами (Знищені БПЛА)': 0,
    'Дерево-мобілі(Знищена автомобільна техніка)': 0,
    'Фритюрниці (Знищені цистерни)': 0,
    'Корита що йдут нах%й (Знищені кораблі)': 0,
    'Спец.металобрухт (Знищена Спец.Техніка)': 0,
    'Вдосконалені гівномети (Знищені пуск. установки ОТРК)': 0,
    }


for key in new_losses.keys():
    while True:
        value = input(f'{key}: '.strip())
        if value.isdigit():
            new_losses[key] = int(value)
            break
        print('Приймає лише integer!')


def calculator_of_rus_losses(new_losses: dict) -> None:
    '''Ця функція порівнює втрати ворога за минулу добу та позаминулу, і виводить різницю втрат, якщо вони були.
    '''
    with open(file_loss, 'r') as old_loss:
        old_losses = {line.split(': ')[0].strip() : int(line.split(': ')[1][:-2]) for line in old_loss}
        print(beginning)
        for key in old_losses.keys():
            if new_losses[key] - old_losses[key]:
                losses =  f'{key}: було: {old_losses[key]}, стало:{new_losses[key]}. + {new_losses[key] - old_losses[key]};'
            else:
                losses = f'{key}: {old_losses[key]} -- нічого не змінилось =('
            print(f'| {losses}' + (93 - len(losses)) * ' ' + '|')

        print(end)

    with open(file_loss, 'w') as old_loss:
        for key, value in new_losses.items():
            old_loss.write(f'{key}: {value} \n')
    
    return 'СЛАВА УКРАЇНІ!'


try:
    calculator_of_rus_losses(new_losses)
except FileNotFoundError:
    phrases = (
        'У вас відсутній файл з назвою "old_losses.txt" біля файла програми.',
        'Створюємо цей файл.',
        'Файл з назвою "old_losses.txt" створено!',
        'Перезапустіть скріпт та впишіть оновленні данні втрат.',
        )
    print()
    print('-' * 96)
    for phrase in phrases[:-2]:
        time.sleep(1)
        print(phrase)
    for dot in range(3):
        time.sleep(0.4), print('.',end=''),
    print()
    with open(file_loss, 'w') as old_loss:
         for key, value in new_losses.items():
             old_loss.write(f'{key}: {value} \n')
    for phrase in phrases[2:]:
        time.sleep(1)
        print(phrase)
    print('-' * 96)