# Родительский класс
class Hero:
    """Класс героя"""
    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты объекта|экземпляра класса
        self.hero_name = name
        self.hero_lvl = lvl
        self.hero_hp = hp

    def base_action(self):
        print(f"{self.hero_name} base action!!")


class MageHero(Hero):
    """Дочерний класс на основе Hero"""

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.hero_mp = mp

    def base_action(self):
        print(f" i'm {self.hero_name} my lvl {self.hero_lvl}")

    def cast_spell(self):
        print("Fire bool!!")

kirito = Hero("Kirito", 100, 1000)
gendalf = MageHero("Gendalf", 100, 10000, 200)

# kirito.base_action()
# gendalf.base_action()
class Swim:
    def action(self):
        print("Swim")

class Fly:
    """Fly"""
    def action(self):
        print("Fly")

class Animal(Swim, Fly):
    """Animal"""
    def action(self):
        print("Krya")

duck = Animal()
# duck.action()
# print(Animal.mro())

class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        super().action()
        print("B")
class C(A):
    def action(self):
        super().action()
        print("C")
class D(C,B):
    def action(self):
        super().action()
        print("D")
        
test_obj = D()
print(D.mro())