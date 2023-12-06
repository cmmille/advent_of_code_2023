from boat_racer import BoatRacer

# Day 06: Part 01
boat_racer = BoatRacer('./input.txt')
print(f"Margin of Error: {boat_racer.run()}")

# Day 06: Part 02
boat_racer = BoatRacer('./input.txt', read_as_single_race=True)
print(f"Margin of Error: {boat_racer.run()}")