while True:
    d = Decimal(input("введите диаметр окружности не более 1000\n"))
    if d > 1000 or d < 0:
        print("введите корректный диаметр от 0 до 1000")
    else:
        break
decimal.getcontext().prec = 42
l = 2 *Decimal(math.pi) * Decimal(d/2)
s = Decimal(math.pi) * Decimal(d/2**2)
print (f'длина окружности = {l}, площадь окружности = {s}')
print(len(str(l)), len(str(s)))
