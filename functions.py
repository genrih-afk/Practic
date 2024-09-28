class Person:
    def __init__(self, name, surname, apartment_number):
        self.name = name
        self.surname = surname
        self.apartment_number = apartment_number

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Квартира: {self.apartment_number}"

    def set_person(self, name, surname, apartment_number):
        self.name = name
        self.surname = surname
        self.apartment_number = apartment_number

    def get_person(self):
        return {"name": self.name, "surname": self.surname, "apartment_number": self.apartment_number}


class Group:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def remove_member(self, person):
        if person in self.members:
            self.members.remove(person)
        else:
            print(f"Person {person.name} {person.surname} is not in the group.")

    def print_members(self):
        print(f"Members of group {self.name}:")
        for member in self.members:
            print(member)

def read_apartments_from_file(filename):
    apartments = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            street, house_number, apartment_number, rooms, floor = line.strip().split(",")
            if street not in apartments:
                apartments[street] = []
            apartments[street].append(
                {
                    "house_number": house_number,
                    "apartment_number": int(apartment_number),
                    "rooms": int(rooms),
                    "floor": int(floor),
                }
            )
    return apartments

def print_apartments_recursive(apartments, street, filename, level=0):
    if street in apartments:
        with open(filename, "a", encoding="utf-8") as file:
            for apartment in apartments[street]:
                file.write(
                    f"{' ' * level * 4}Квартира: {apartment['apartment_number']}, {apartment['rooms']} комнаты, этаж {apartment['floor']}"
                )
    else:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{' ' * level * 4}Квартир на улице {street} не найденоn")


def sort_apartments_by_number(apartments, street, house_number):
    if street in apartments:
        house_apartments = [
            apartment
            for apartment in apartments[street]
            if apartment["house_number"] == house_number
        ]
        for i in range(1, len(house_apartments)):
            key = house_apartments[i]
            j = i - 1
            while j >= 0 and house_apartments[j]["apartment_number"] > key["apartment_number"]:
                house_apartments[j + 1] = house_apartments[j]
                j -= 1
            house_apartments[j + 1] = key
        return house_apartments
    else:
        return []

def binary_search_apartment(apartments, street, house_number, apartment_number):
    sorted_apartments = sort_apartments_by_number(apartments, street, house_number)
    left = 0
    right = len(sorted_apartments) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_apartments[mid]["apartment_number"] == apartment_number:
            return mid
        elif sorted_apartments[mid]["apartment_number"] < apartment_number:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def add_apartment(filename, street, house_number, apartment_number, rooms, floor):
    """
    Добавляет адрес в файл с адресами.
    """
    apartments = read_apartments_from_file(filename)
    if street not in apartments:
        apartments[street] = []  # Добавляем новый ключ в словарь
    apartments[street].append(
        {
            "house_number": house_number,
            "apartment_number": int(apartment_number),
            "rooms": int(rooms),
            "floor": int(floor),
        }
    )
    with open(filename, "w", encoding="utf-8") as file:
        for street_name, houses in apartments.items():
            for apartment in houses:
                file.write(
                    f"{street_name},{apartment['house_number']},{apartment['apartment_number']},{apartment['rooms']},{apartment['floor']}\n"
                )


def delete_apartment(filename, street, house_number, apartment_number):
    """
    Удаляет адрес из файла с адресами.
    """
    apartments = read_apartments_from_file(filename)
    if street in apartments:
        apartments[street] = [
            apartment
            for apartment in apartments[street]
            if not (
                apartment["house_number"] == house_number
                and apartment["apartment_number"] == apartment_number
            )
        ]
        with open(filename, "w", encoding="utf-8") as file:
            for street_name, houses in apartments.items():
                for apartment in houses:
                    file.write(
                        f"{street_name},{apartment['house_number']},{apartment['apartment_number']},{apartment['rooms']},{apartment['floor']}\n"
                    )
    else:
        print(f"Квартира на улице {street} не найдена.")

def modify_apartment(filename, street, house_number, apartment_number, new_street=None, new_house_number=None, new_apartment_number=None, new_rooms=None, new_floor=None):
    """
    Изменяет адрес в файле с адресами.
    """
    apartments = read_apartments_from_file(filename)
    if street in apartments:
        for i, apartment in enumerate(apartments[street]):
            if apartment["house_number"] == house_number and apartment["apartment_number"] == apartment_number:
                if new_street:
                    apartments[street][i]["house_number"] = new_house_number
                if new_house_number:
                    apartments[street][i]["house_number"] = new_house_number
                if new_apartment_number:
                    apartments[street][i]["apartment_number"] = new_apartment_number
                if new_rooms:
                    apartments[street][i]["rooms"] = new_rooms
                if new_floor:
                    apartments[street][i]["floor"] = new_floor
                with open(filename, "w", encoding="utf-8") as file:
                    for street_name, houses in apartments.items():
                        for apartment in houses:
                            file.write(
                                f"{street_name},{apartment['house_number']},{apartment['apartment_number']},{apartment['rooms']},{apartment['floor']}\n"
                            )
                break
        else:
            print(f"Квартира {apartment_number} в доме {house_number} на улице {street} не найдена.")
    else:
        print(f"Квартир на улице {street} не найдено.")