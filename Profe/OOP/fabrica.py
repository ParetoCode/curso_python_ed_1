from workers.tailor import Tailor
from workers.tshirt_specialist import Tshirt_specialist
from machines.sewing_machine import Sewing_machine

PIECE = {'measure': 5, 'kind': 'T-shirt'}

singed = Sewing_machine()
agapito = Tailor(singed, 45000)
agapito.sew_on_zigag(PIECE)
agapito.measure(PIECE)
agapito.change_thread()
print(agapito.salary)

machine = Sewing_machine()
ataulfa = Tshirt_specialist(machine, 55000)

ataulfa.sew_straight()
ataulfa.change_thread()
print(ataulfa.experience_years)

