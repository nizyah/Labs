numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_begin = numbers[0:4]
numbers_end = numbers[5:]
numbers_ = numbers_begin + numbers_end

total = sum(numbers_)
count = len(numbers)
none = total / count
none_ = [none]

numbers_new = numbers_begin + none_ + numbers_end
print("Измененный список:", numbers_new)
