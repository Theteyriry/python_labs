import re
with open('text.txt', 'r', encoding='utf-8') as f:
    dates = re.findall(r'\b(\d{2})\.(\d{2})\.(\d{4})\b', f.read())
# Преобразование и сортировка дат
sorted_dates = sorted([f"{year}-{month}-{day}" for day, month, year in dates], 
                     key=lambda x: tuple(map(int, x.split('-'))))
# Сохранение результатов
with open('dates.txt', 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(sorted_dates))
print("Даты успешно обработаны и сохранены в файл dates.txt")