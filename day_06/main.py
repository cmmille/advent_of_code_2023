from boat_racer import BoatRacer

# Day 06: Part 01
boat_racer = BoatRacer('./input.txt')
print(f"Margin of Error: {boat_racer.calc_all_possible_wins()}")