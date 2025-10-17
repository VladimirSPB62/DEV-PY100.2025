money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

current_budget = money_capital + salary  # Бюджет текущего месяца
count_month = 0  # Счетчик месяцев

while current_budget > spend: # Цикл повторяется пока бюджет больше расходов
    count_month += 1  # После каждого цикла увеличиваем счетчик
    current_budget -= spend  # Вычитаем текущие траты
    spend += spend * increase  # Учитываем ежемесячный рост цен
    current_budget += salary  # Получаем зарплату

print("Количество месяцев, которое можно протянуть без долгов:", count_month)
