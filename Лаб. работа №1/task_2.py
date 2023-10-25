weight = 4
symvol = 25
stroka = 50
page = 100
vsego = 1.44 * 1024 ** 2

book_weight = page * stroka * symvol * weight
count = int(vsego / book_weight)

print("Количество книг, помещающихся на дискету:", count)
