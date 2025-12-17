fio = input("Введите фамилию, имя и отчество: ")

parts = fio.split() # разделяю строки

if len(parts) != 3:
    print("Ошибка: введите фамилию, имя и отчество через пробелы.")
else:
    surname = parts[0]  # Фамилия
    name = parts[1]     # Имя
    middle_name = parts[2]  # Отчество

    print("Имя:", name)
    print("Отчество:", middle_name)

    letters_in_surname = len(surname) # Количество букв в фамилии
    print("Количество букв в фамилии:", letters_in_surname)
