from classes.game import Game
from classes.cube_collection import CubeCollection

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        all_games = [Game(line) for line in lines]
        bag = CubeCollection(12, 13, 14)
        # [print(f"{game.id}: {game.is_possible(bag)}") for game in all_games]
        valid_ids = [game.id for game in all_games if game.is_possible(bag)]
        sum_of_valid_ids = sum(valid_ids)
        print(f"Sum of valid ids: {sum_of_valid_ids}")
        
def demo():
    process_file('input/demo.txt')
    
def part_01():
    print("Part 01:")
    process_file('input/input.txt')

if __name__ == "__main__":
    # demo()
    process_file('input/input.txt')