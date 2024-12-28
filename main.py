class House:
    def __init__(self, name, floor_numb):
        self.name = name
        self.floor_numb = floor_numb

    def go_to(self, new_floor):
        floor = 0
        print(f'Здание {self.name}, имеет   {self.floor_numb} этажа \пПоднимаемся на {new_floor}')
        if new_floor < 1 or  new_floor > self.floor_numb:
            print(f'{new_floor} - такого этажа не существует')
        else:
           for floor in range(new_floor):
            print(floor + 1)

    def __len__(self):
        return self.floor_numb

    def __str__(self):
        title = str(f'Название: {self.name}, количество этажей: {self.floor_numb}')
        return title

hightower = House('Башня', 12)
warehouse = House('Склад', 4)

print(hightower)
print(warehouse)

print(len(hightower))
print(len(warehouse))


