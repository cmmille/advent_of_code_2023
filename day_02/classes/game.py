from classes.cube_collection import CubeCollection

class Game():
    def __init__(self, line):
        self.read_sets_from_line(line)
    
    def __str__(self) -> str:
        return f"Id: {self.id}, Rounds: {[str(round) for round in self.rounds]}"
    
    def parse_set(self, set):
        raw_cubes = set.split(',')
        # for each cube, split on space.
        # first element is number, second is color
        return {cube.split()[1]: int(cube.strip().split()[0]) for cube in raw_cubes}
        

    def read_sets_from_line(self, line):
        raw_id, raw_sets = line.strip().split(':')
        rounds = [self.parse_set(set.strip()) for set in raw_sets.split(';')]
        self.rounds = [CubeCollection(**round) for round in rounds]
        self.id = int(raw_id.split()[1])

    def minimum_cubes(self):
        max_red = max([round.red for round in self.rounds])
        max_blue = max([round.blue for round in self.rounds])
        max_green = max([round.green for round in self.rounds])
        return CubeCollection(max_red, max_blue, max_green)
        
    def is_possible(self, bag):
        return all([round.is_possible(bag) for round in self.rounds])