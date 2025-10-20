from Dog import Dog


class HomeDog(Dog):

    def __init__(self, name, owner, age, breed, hair_colour):
        super().__init__(age, breed, hair_colour)
        self.name = name
        self.owner = owner