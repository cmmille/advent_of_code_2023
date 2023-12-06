class BoatRacer:
    # Constructor
    def __init__(self, file_path):
        self.file_path = file_path
        self.read_file()
    
    def read_file(self):
        with open(self.file_path, 'r') as f:
            raw_data = f.read().splitlines()
        self.times = raw_data[0].split()[1:]
        self.distances = raw_data[1].split()[1:]
    
    def calc_distance_traveled(self, race_time, time_button_held):
        # distance_traveled = (race_time - time_button_held) * time_button_held
        return (race_time - time_button_held) * time_button_held
    
    def race_won(self, distance_traveled, record_distance):
        return distance_traveled > record_distance
    
    def all_possible_distances(self, race_time):
        return [self.calc_distance_traveled(race_time, x) for x in range(race_time + 1)]
    
    def all_winning_races(self, race_time, record_distance):
        # Find all possibilities of button held to beat the record distance
        # Return a list of all the times the button should be held
        # Return an empty list if no times can beat the record distance
        return [x for x in self.all_possible_distances(race_time) if self.race_won(x, record_distance)]
    
    def count_winning_possibilities(self, race_time, record_distance):
        return len(self.all_winning_races(race_time, record_distance))
    
    def calc_all_possible_wins(self):
        margin_of_error = 1
        for i, race_time in enumerate(self.times):
            record_distance = int(self.distances[i])
            possibles = self.count_winning_possibilities(int(race_time), record_distance)
            margin_of_error *= possibles
        return margin_of_error