money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital + salary
month = 0

while spend < budget:
    month += 1
    spend *= (1 + increase)
    budget += salary
    budget -= spend

print("Количество месяцев, которое можно протянуть без долгов:", month)
