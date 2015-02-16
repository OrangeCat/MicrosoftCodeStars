class Person:
    """
    Класс человека
    """
    name = "No name"

    def __init__(self, name=""):
        self.name = name

    def present(self):
        print('My name is {0}'.format(self.name))

    def say(self):
        print('Bla-bla-bla')


class SuperPerson(Person):

    def __init__(self, name):
        Person.__init__(self, name)

    def present(self):
        print("I'm SUPER Person!!!! My name is {0}".format(self.name))


p1 = Person("Alex")

p = SuperPerson("Alex")

p.present()
p.say()

print("develop")