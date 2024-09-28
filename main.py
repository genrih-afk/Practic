from functions import *

def main():
    """
    Основной файл с меню.
    """
    apartments = read_apartments_from_file("apartments.txt")

    # Создаем группу
    group_a = Group("Группа А")

    # Создаем несколько персон
    person1 = Person("Иван", "Иванов", 10)
    person2 = Person("Мария", "Петрова", 20)
    person3 = Person("Петр", "Сидоров", 30)


    while True:
        print("nМеню:")
        print("1. Вывести информацию о квартирах на улице")
        print("2. Сортировать квартиры в доме по номеру")
        print("3. Выполнить бинарный поиск номера квартиры")
        print("4. Добавить новый адрес")
        print("5. Удалить адрес")
        print("6. Изменить адрес")
        print("7. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            street = input("Введите название улицы: ")
            output_filename = input("Введите имя файла для вывода: ")
            print_apartments_recursive(apartments, street, output_filename)
            print(f"Информация о квартирах на улице {street} записана в файл {output_filename}.")
        elif choice == "2":
            street = input("Введите название улицы: ")
            house_number = input("Введите номер дома: ")
            sorted_apartments = sort_apartments_by_number(apartments, street, house_number)
            if sorted_apartments:
                print("Отсортированный список квартир в доме:")
                for apartment in sorted_apartments:
                    print(
                        f"Квартира: {apartment['apartment_number']}, {apartment['rooms']} комнаты, этаж {apartment['floor']}"
                    )
            else:
                print(f"Квартир в доме {house_number} на улице {street} не найдено.")
        elif choice == "3":
            street = input("Введите название улицы: ")
            house_number = input("Введите номер дома: ")
            apartment_number = int(input("Введите номер квартиры для поиска: "))
            index = binary_search_apartment(apartments, street, house_number, apartment_number)
            if index != -1:
                print(f"Квартира {apartment_number} найдена в доме {house_number} на улице {street}."
                )
            else:
                print(
                    f"Квартира {apartment_number} не найдена в доме {house_number} на улице {street}."
                )

        elif choice == "4":
            street = input("Введите название улицы: ")
            house_number = input("Введите номер дома: ")
            apartment_number = int(input("Введите номер квартиры: "))
            rooms = int(input("Введите количество комнат: "))
            floor = int(input("Введите этаж: "))
            add_apartment("apartments.txt", street, house_number, apartment_number, rooms, floor)
            print("Адрес добавлен.")
        elif choice == "5":
            street = input("Введите название улицы: ")
            house_number = input("Введите номер дома: ")
            apartment_number = int(input("Введите номер квартиры: "))
            delete_apartment("apartments.txt", street, house_number, apartment_number)
        elif choice == "6":
            street = input("Введите название улицы: ")
            house_number = input("Введите номер дома: ")
            apartment_number = int(input("Введите номер квартиры: "))
            print("Введите новые данные (оставьте поле пустым, если не хотите изменять):")
            new_street = input("Новая улица: ")
            new_house_number = input("Новый номер дома: ")
            new_apartment_number = input("Новый номер квартиры: ")
            new_rooms = input("Новое количество комнат: ")
            new_floor = input("Новый этаж: ")
            modify_apartment("apartments.txt", street, house_number, apartment_number, new_street, new_house_number,
                             new_apartment_number, new_rooms, new_floor)
        elif choice == "7":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
     main()