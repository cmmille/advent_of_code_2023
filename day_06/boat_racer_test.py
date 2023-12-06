import unittest
from boat_racer import BoatRacer

class TestBoatRacer(unittest.TestCase):
    def test_calc_distance_traveled(self):
        boat_racer = BoatRacer('./dummy_input.txt')  # Create an instance of BoatRacer
        self.assertEqual(boat_racer.calc_distance_traveled(7, 0), 0)
        self.assertEqual(boat_racer.calc_distance_traveled(7, 1), 6)
        self.assertEqual(boat_racer.calc_distance_traveled(7, 2), 10)
        self.assertEqual(boat_racer.calc_distance_traveled(7, 3), 12)
        self.assertEqual(boat_racer.calc_distance_traveled(7, 4), 12)
        self.assertEqual(boat_racer.calc_distance_traveled(7, 5), 10)
        self.assertEqual(boat_racer.calc_distance_traveled(7, 6), 6)
        self.assertEqual(boat_racer.calc_distance_traveled(7, 7), 0)
    
    def calc_all_possible_wins(self):
        boat_racer = BoatRacer('./dummy_input.txt')
        self.assertEqual(boat_racer.calc_all_possible_wins(), 288)

if __name__ == '__main__':
    unittest.main()