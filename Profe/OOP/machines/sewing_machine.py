class Sewing_machine:
    brand = 'Singer'

    def zigzag_sew(self, piece):
        kind_of_piece = piece.get('kind')
        print(f"I'm sewing on zigzag {kind_of_piece}")

    def straight_sew(self, piece):
        kind_of_piece = piece.get('kind')
        print(f"I'm sewing on straight line {kind_of_piece}")

    def change_thread(self):
        print('IM CHANGING THE THREAD PLEASE HOLD ON')