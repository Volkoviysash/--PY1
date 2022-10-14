money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while True:
    # Вычитаем траты с капитала
    money_capital -= spend

    # Если капитал отрицательный - закончить цикл
    if money_capital <= 0:
        break

    # Если капитал положительный, добавить к нему зарплату
    money_capital += salary

    # Добавить к количеству месяцев 1
    month += 1

    # Увеличить затраты на инфляцию
    spend += spend * increase

print(month)
