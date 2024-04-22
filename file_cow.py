from cow import Cow


class FileCow(Cow):
    def __init__(self, name, filename):
        super().__init__(name)
        try:
            self.image = open(filename, 'r').read()
        except Exception:
            raise RuntimeError("MOOOOO!!!!!!")

    def set_image(self, image):
        raise RuntimeError("cannot rest FileCow Image")
