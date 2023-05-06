from .tailor import Tailor

class Tshirt_specialist(Tailor):
    tshirt = {'kind': 'T-shirt', 'measure': 0.2}

    def sew_straight(self):
        super().sew_straight(self.tshirt)

