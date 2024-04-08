from cow import Cow


class Dragon(Cow):
    # init all variables
    def __init__(self, name, image):
        super().__init__(name)
        self.name = name
        self.image = image

    def can_breathe_fire(self):
        return True
