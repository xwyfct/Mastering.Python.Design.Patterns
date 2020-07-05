#!/usr/bin/python
# -*- coding:utf8 -*-


class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(
            '{frog_name} the Frog encounters {obstacle} and {action}!'.format(
                frog_name=self, obstacle=obstacle, action=obstacle.action()))


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


# 抽象工厂
class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------Frog World -----'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard batteles against {} and {}!'.format(
            self, obstacle, obstacle.action()))


class Ork:
    def __str__(self):
        return 'an evial ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------Wizard World-----'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


# 游戏主入口
class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input('Welcome {}. How old are you ?'.format(name))
        age = int(age)
    except ValueError:
        print("Age {} is valid, plz try again...".format(age))
        return (False, age)
    return (True, age)


def main():
    name = input("Hello, What is your name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
        game = FrogWorld if age < 18 else WizardWorld
        environment = GameEnvironment(game(name))
        environment.play()


if __name__ == "__main__":
    main()
