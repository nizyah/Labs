def find_common_participants(group_one, group_two, separator=","):
    group_one_set = set(group_one.split(separator))
    group_two_set = set(group_two.split(separator))
    common = list(group_one_set.intersection(group_two_set))
    common.sort()
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Общие участники: ", find_common_participants(participants_first_group, participants_second_group, separator="|"))
