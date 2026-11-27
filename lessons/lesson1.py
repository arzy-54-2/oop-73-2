# HeroMage
# hero_mage

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

# Объект на основе класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 101, 1002)
my_str = "text"
my_int = 123

# print(type(my_str))
# print(type(kirito))

# my_str.capitalize()
# my_int.bit_count()
# kirito.base_action()

# kirito.base_action()
# asuna.base_action()
# print(asuna.hero_name, asuna.hero_lvl, asuna.hero_hp)
