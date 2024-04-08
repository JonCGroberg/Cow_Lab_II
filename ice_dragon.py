class IceDragon:
    # init all variables to None
    def __init__(self, name):
        self.name = name
        self.image = None

    # return Cow name

    def get_name(self):
        return self.name

    # return Cow image

    def get_image(self):
        return self.image

    # set Cow image

    def set_image(self, image):
        self.image = image
