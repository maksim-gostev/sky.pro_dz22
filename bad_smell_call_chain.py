# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, city_population, room_num):
        self.city_population = city_population
        self.room_num = room_num

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.