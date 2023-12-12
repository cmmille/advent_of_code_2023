from classes.game import Game
from classes.cube_collection import CubeCollection

def sum_valid_ids(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        all_games = [Game(line) for line in lines]
        bag = CubeCollection(12, 13, 14)
        valid_ids = [game.id for game in all_games if game.is_possible(bag)]
        sum_of_valid_ids = sum(valid_ids)
        print(f"Sum of valid ids: {sum_of_valid_ids}")

def sum_minimum_cube_products(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        all_games = [Game(line) for line in lines]
        minimum_cubes = [game.minimum_cubes() for game in all_games]
        minimum_cube_products = [cube.product() for cube in minimum_cubes]
        sum_of_minimum_cube_products = sum(minimum_cube_products)
        print(f"Sum of minimum cube products: {sum_of_minimum_cube_products}")
        
def demo():
    print("Demo:")
    sum_valid_ids('input/demo.txt')
    sum_minimum_cube_products('input/demo.txt')
    
def part_01():
    print("Part 01:")
    sum_valid_ids('input/input.txt')

def part_02():
    print("Part 02:")
    sum_minimum_cube_products('input/input.txt')

if __name__ == "__main__":
    demo()
    part_01()
    part_02()