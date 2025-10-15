# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
# Создаем словарь посещений.
site_statistic = {
    'Общее количество': 0,
    'Уникальные посещения': 0
}

total_visit = len(users)  # Количество общих посещений.
unique_visit = len(set(users))  # Количество уникальных посещений.

# Исправляем данные в словаре.
site_statistic['Общее количество'] = total_visit
site_statistic['Уникальные посещения'] = unique_visit

print(site_statistic)
