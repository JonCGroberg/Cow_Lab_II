from dragon import Dragon


class IceDragon(Dragon):
    # init all variables to None
    def __init__(self, name, image):
        super().__init__(name, image)

    def can_breathe_fire(self):
        return False
