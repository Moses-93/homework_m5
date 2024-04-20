import sys
from collections import Counter

def parse_log_line(line: str) -> dict: # Функція для парсингу логфайлів 
    format_line = line.split()
    date = format_line[0] + " " + format_line[1]
    level = format_line[2]
    message = " ".join(format_line[3:]) 
    return {"date": date, 
            "level": level, 
            "message": message}

def load_logs(file_path: str) -> list: # функція для завантаження логфайлів  
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file_log:
            for line in file_log:
                logs.append(parse_log_line(line))
    except FileNotFoundError as error:
        print(f"Файл з таким іменем не знайдено: {error}")
    except PermissionError as error:
        print(f"Немає доступу до файлу: {error}")
    except Exception as error:
        print(f"Помилка при читанні файлу логів: {error}")
    if not logs:
        print("Файл логів порожній")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list: # функція для фільтрації логфайлів
    return [dicts for dicts in logs if dicts["level"] == level]

def count_logs_by_level(logs: list) -> dict: # функція дл підрахунку кількості рівнів логів
    count_level = [dicts["level"] for dicts in logs]
    counter = Counter(count_level)
    return counter

def display_log_counts(counts: dict): # функція для виведення кількості рівнів логів
    for key, value in counts.items():
        print(f"{key}: {value}")

def main(): # функція для запуску програми
    if len(sys.argv) < 2:
        print("Потрібно вказати шлях до файлу логів як аргумент командного рядка.")
        return    
    path_logfile = sys.argv[1].upper()
    list_logfile = load_logs(path_logfile)
    
    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        if level not in ["INFO", "WARNING", "ERROR", "DEBUG"]:
            print("Такого рівня логів не існує.")
            return
        filtered_logs = filter_logs_by_level(list_logfile, level)  
        print(f"Деталі логів для рівня: {level}")
        for dicts in filtered_logs:
            print(dicts["date"] + " - " + dicts["message"])
    else:
        counts = count_logs_by_level(list_logfile)
        display_log_counts(counts)

if __name__ == "__main__":
    main()