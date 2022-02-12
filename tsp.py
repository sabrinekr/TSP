import gym
from omegaconf import DictConfig
from copy import copy, deepcopy
from city import City

class TSP(gym.Env):
    """This class represents the TSP environment"""


    def __init__(self, config: DictConfig) -> None:
        self.file_path = config["data_file_path"]
        self.cities = load_data(self.file_path)
        self.cities_cache = deepcopy(self.cities)

    def reset(self):
        self.cities = self.cities_cache

    def step(self, indx: int):
        return None

def load_data(file_path)-> list:
    lines = []
    with open(file_path) as f:
        lines = f.readlines()
    cities_list = [ line.split() for line in lines if line[0].isnumeric()]
    cities = [City(city[0], city[1], city[2]) for city in cities_list]

    return cities
