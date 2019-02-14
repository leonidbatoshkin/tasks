class Pet(object):
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, "и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food=4):
        print("Мрр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        rep = "Объект класса Pet\n"
        rep += f"имя: {self.name}, голод: {str(self.hunger)}, настроение: {str(self.boredom)}"
        return rep

    @staticmethod
    def main():
        pet_name = input("Как вы назовёте свою зверушку?")
        my_pet = Pet(pet_name)
        choice = None
        while choice != "0":
            print("""
            Моя зверюшка
            0 - Выйти
            1 - Узнать о самочувствии зверюшки
            2 - Покормить зверюшку
            3 - Поиграть со зверюшкой
            """)
            choice = input("Ваш выбор: ")
            print()
            if choice == "0":
                print("До свидания.")
            elif choice == "1":
                my_pet.talk()
            elif choice == "2":
                my_pet.eat()
            elif choice == "3":
                my_pet.play()
            elif choice == "scrt":
                print(my_pet)
            else:
                print("Извините, в меню нет пункта", choice)


if __name__ == '__main__':
    Pet.main()