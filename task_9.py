salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
while months > 0:
    # Разница зарплаты и затрат (по сути долг, который накапливается)
    delta = salary - spend
    # Количество денег минус дельта - положительное число, так как дельта - отрицательная
    need_money -= delta

    months -= 1
    spend += spend*increase
    
print(round(need_money))
