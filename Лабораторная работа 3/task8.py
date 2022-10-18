money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while True:
    money_capital = money_capital - spend
    if money_capital < 0:
        break
    money_capital += salary
    month += 1
    spend += spend * increase

print(month)
