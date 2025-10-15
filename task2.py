# TODO Разделите участников на две команды
list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Количество игроков в списке.
num = len(list_players)

# Делим игроков на команды.
part = num // 2
players1 = list_players[:part]
players2 = list_players[part:]

print(players1)
print(players2)
