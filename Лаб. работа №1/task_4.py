users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

sum_ = len(users)
unique = len(set(users))

stats = {"Общее количество": 0, "Уникальные посещения": 0}

stats["Общее количество"] = sum_
stats["Уникальные посещения"] = unique

print(stats)
