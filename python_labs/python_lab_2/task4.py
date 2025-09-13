#добавляем модуль для работы с регулярными выражениями
import re
#открываем файл text в формате чтения, расшифровываем в формате utf-8, в дальнейшей работе text называем f
with open('text.txt', 'r', encoding='utf-8') as f:
     #вводим переменную text для хранения прочитанных из f данных
     text = f.read()
#вводим переменную для поиска email по шаблону
#r' позволяет дополнительно не экранировать слэш (то есть \. для точки, а не \\.)
#\b - границы выражения (не считывает подходящие выражения в составе не подходящих типа cat в category или call в recall)
#в квадратных скобках с + диапазон обязательных знаков(один или более из них)
#{2,} - минимум 2 символа из диапазона [A-Za-z], тк минимально возможное ru
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
#re.findall записывает все подходящие по формату email-а из переменной text в переменную emails
emails = re.findall(email_pattern, text)
#\d{3} - ровно 3 цифры
phone_pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}'
phones = re.findall(phone_pattern, text)
#слово обязательно начинается ровно с одной заглавной буквы [A-ZА-Я], а далее содержит 0 или более символов (цифры, заглавные и строчные буквы, дефис)
capital_words_pattern = r'\b[A-ZА-Я][A-ZА-Яa-zа-я0-9-]*\b'
capital_words = re.findall(capital_words_pattern, text)
#открываем (или создаем, если ещё нет) файл emails.txt в режиме записи под именем f_e
with open('emails.txt', 'w', encoding='utf-8') as f_e:
    #перебираем все значения в переменной emails и записываем каждый элемент в файл
    for email in emails:
        #'\n' - перенос на новую строку, чтобы все адреса были в отдельных строчках
        f_e.write(email + '\n')
with open('phones.txt', 'w', encoding='utf-8') as f_p:
    for phone in phones:
        f_p.write(phone + '\n')
with open('capital_words.txt', 'w', encoding='utf-8') as f_c:
    for word in capital_words:
        f_c.write(word + '\n')
#выводим сообщение об успешном создании файла с содержимым (или перезаписи содержимого)
print("Email-адреса сохранены в файл emails.txt")
print("Номера телефонов сохранены в файл phones.txt")
print("Слова с заглавной буквы сохранены в файл capital_words.txt")