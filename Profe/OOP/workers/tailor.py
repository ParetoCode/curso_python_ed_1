class Tailor:
    experience_years = 4
    age = 21
    
    def __init__(self, sweing_machine, salary_in_euro):
        self.sweing_machine = sweing_machine
        self.salary = salary_in_euro

    def measure(self, piece):
        textil_measure = piece.get('measure')
        print(f'The measure is {textil_measure} m')

    def sew_on_zigag(self, piece):
        self.sweing_machine.zigzag_sew(piece)

    def sew_straight(self, piece):
        self.sweing_machine.straight_sew(piece)

    def change_thread(self):
        self.sweing_machine.change_thread()