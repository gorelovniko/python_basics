"""
6. *Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно,
 т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
   (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
   (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
   (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

goods = []
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
for i in range(1, 4):
    goods.append(
        (i, {
             'name': input("Введите наименование товара: "),
             'price': float(input("Введите стоимость товара: ")),
             'quantity': int(input("Введите количество товара: ")),
             'unit': input("Введите единицу измерения товара: ")
         })
    )
for product in goods:
    analytics['name'].append(product[1]['name'])
    analytics['price'].append(product[1]['price'])
    analytics['quantity'].append(product[1]['quantity'])
    analytics['unit'].append(product[1]['unit'])
print('Список товаров: ')
for f in goods:
    print(f)
print('Список аналитики: ')
for key, value in analytics.items():
    print(key, ':', value)
