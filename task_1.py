def caching_fibonacci():
    # Ініціалізувати словник кешу для зберігання раніше обчислених чисел Фібоначчі
    cache = {}
    def fibonacci(n):
        try:
            # Базові випадки: повернути 0 для n = 0 та 1 для n = 1
            if n == 0:
                return 0
            if n == 1:
                return 1
            # Перевірити, чи вже є число Фібоначчі для n у кеші
            if n in cache:
                return cache[n]
            # Якщо ні, обчислити його та зберегти в кеші
            else:
                cache[n] = fibonacci(n-1) + fibonacci(n-2)
                print(cache[n])
                return cache[n]
        # Обробити виняток, якщо n не є цілим числом
        except TypeError:
            print("Помилка: вхідне значення має бути цілим числом.")
            return None

    return fibonacci

res = caching_fibonacci()

