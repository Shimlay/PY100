salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
money_capital = 0  # начальная сумма на счету
months = 0  # количество месяцев, которые можно прожить

while months < 10:
    months += 1
    money_capital += salary - spend  # пересчет суммы на счету
    spend *= 1.03
print(round(abs(money_capital)))
