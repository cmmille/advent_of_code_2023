class BoatRacer:
    """
    The BoatRacer class represents a boat racer who competes in races.

    Attributes:
        file_path (str): The path to the file containing race data.
        times (list): A list of times for each race.
        distances (list): A list of distances for each race.

    Methods:
        run(): Calculates all possible wins for all races.
    """
    def __init__(self, file_path, read_as_single_race=False):
        """
        Initialize BoatRacer with a file path and an optional flag to read all races as one.
        """
        self.file_path = file_path
        self.__read_file()
        if read_as_single_race:
            self.__read_as_single_race()

    def __read_file(self):
        """
        Read the file and split the data into times and distances.
        """
        with open(self.file_path, 'r') as f:
            raw_data = f.read().splitlines()
        self.times = raw_data[0].split()[1:]
        self.distances = raw_data[1].split()[1:]

    def __calc_distance_traveled(self, race_time, time_button_held):
        """
        Calculate the distance traveled given the race time and the time the button was held.
        """
        return (race_time - time_button_held) * time_button_held

    def __race_won(self, distance_traveled, record_distance):
        """
        Determine if the race was won given the distance traveled and the record distance.
        """
        return distance_traveled > record_distance

    def __all_possible_distances(self, race_time):
        """
        Calculate all possible distances given the race time.
        """
        return [self.__calc_distance_traveled(race_time, x) for x in range(race_time + 1)]

    def __all_winning_races(self, race_time, record_distance):
        """
        Find all winning races given the race time and the record distance.
        """
        return [x for x in self.__all_possible_distances(race_time) if self.__race_won(x, record_distance)]

    def __count_winning_possibilities(self, race_time, record_distance):
        """
        Count the number of winning possibilities given the race time and the record distance.
        """
        return len(self.__all_winning_races(race_time, record_distance))

    def __read_as_single_race(self):
        """
        Read the times and distances as a single line.
        """
        self.times = [f"{''.join(self.times)}"]
        self.distances = [f"{''.join(self.distances)}"]

    def run(self):
        """
        Calculate total number of ways the race could be won.
        """
        margin_of_error = 1
        for i, race_time in enumerate(self.times):
            record_distance = int(self.distances[i])
            possibles = self.__count_winning_possibilities(int(race_time), record_distance)
            margin_of_error *= possibles
        return margin_of_error