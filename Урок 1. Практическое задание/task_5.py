"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""

profit = int(input('Введите значение прибыли: '))
loss = int(input('Введите значение издержек: '))
people = int(input('Ввдите количество работников: '))
if profit > loss:
    print('Выручка больше издержек')
    clear_profit = profit - loss
    rent = clear_profit / profit
    print('Рентабельность {} выручки {}: {:.2f}'
          .format('нашей', 'составила', rent))
    clear_for_person = float(clear_profit / people)
    print(
        'Прибыль фирмы в расчете на одного сотрудника: %s' % clear_for_person)
else:
    print('Фирма работает в убыток')
