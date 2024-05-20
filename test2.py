import math

def find_divisors(n):
    """Находит все делители числа n."""
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Чтобы избежать дублирования, если делители не равны
                divisors.append(n // i)
    return divisors

def common_divisors(numbers):
    """Находит общие делители для массива положительных целых чисел."""
    if not numbers:
        return []

    # Получаем делители для первого числа
    first_divisors = find_divisors(numbers[0])

    # Находим общие делители для всех остальных чисел
    for num in numbers[1:]:
        common_divs = []
        for div in first_divisors:
            if div <= num and num % div == 0:
                common_divs.append(div)
        first_divisors = common_divs

    # Преобразуем в отсортированный список и возвращаем
    return sorted(first_divisors)

# Пример использования:
numbers = [42, 12, 18]
print(common_divisors(numbers))  # [1, 2, 3, 6]