cranesTotal = int(input(
    'введите общее количество журавликов, и рассчитаю сколько сделал каждый ребенок в отдельности: '))


def CranesByChild(number):
    if number % 6 == 0:
        petyaAndSerezha = int(number / 6)
        katya = int(4 * petyaAndSerezha)
        return f"Петя и Сережа сделали по {petyaAndSerezha} журавлику(ов), а Катя - {katya} журавлика(ов)."
    else:
        return "У задачи нет решения"


print(CranesByChild(cranesTotal))
