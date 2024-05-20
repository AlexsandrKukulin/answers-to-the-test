def multiplication_table(number):
    # Проверяем, что число не отрицательное и не больше 10
    if number < 1 or number > 10:
        print("Число должно быть в пределах от 1 до 10.")
        return

    # Выводим заголовок таблицы
    print(' '.join(map(str, range(1, number+1))))

    # Выводим саму таблицу умножения
    for i in range(1, number+1):
        print(' '.join(map(str, [i*j for j in range(1, number+1)])))

# Пример использования метода
multiplication_table(5)