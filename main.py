n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
apples = k // n
ostatok = k % n
print("Каждому школьнику достанется:", apples)
print("Яблок останется в корзинке:", ostatok)
