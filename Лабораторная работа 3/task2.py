def find_common_participants(part1, part2, separator=','):
    common_parts = list(set(part1.split(separator)).intersection(set(part2.split(separator))))
    common_parts.sort()
    return common_parts

first_group = "Иванов|Петров|Сидоров"
second_group = "Петров|Сидоров|Смирнов"

common_group = find_common_participants(first_group, second_group, '|')

print('Общие участники:', common_group)