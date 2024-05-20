# Возвращает массив простых чисел в заданном диапазоне.
    
def prime_numbers_in_range(min_value, max_value): 
    # Создаем список чисел от min_value до max_value включительно
    numbers = list(range(min_value, max_value + 1))
    
    # Фильтруем список, оставляя только простые числа
    prime_numbers = [num for num in numbers if all(num % i for i in range(2, num) if i != num // 2)]
    
    return prime_numbers

# Пример использования функции
prime_numbers = prime_numbers_in_range(11, 20)
print(prime_numbers)  # Выведет: [11, 13, 17, 19]