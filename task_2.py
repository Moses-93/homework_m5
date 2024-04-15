import re  
from typing import Callable  

text = """Загальний дохід працівника
складається з декількох частин: 1000.01 як основний дохід, 
доповнений додатковими надходженнями 27.45 і 324.00 доларів.""" 

def generator_numbers(text: str):  
    try:  # блок try-except для обробки помилок
        pattern = r"\d+\.\d+|\d+"  # Регулярний вираз для знаходження дійсних чисел
        for search in re.finditer(pattern, text):  # Ітерація через всі збіги регулярного виразу в тексті
            yield float(search.group())  # Повертає знайдене число 
    except TypeError:  # Обробка помилки типу даних
            print("Невірний тип даних")  

def sum_profit(text: str, func: Callable):  
    result = sum(func(text))  # Обчислення загальної суми чисел, знайдених функцією-генератором
    return result  # Повернення результату обчислення

total_income = sum_profit(text, generator_numbers)  # Обчислення загального доходу 
print(f"Загальний дохід: {total_income}") 
