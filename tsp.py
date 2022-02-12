import gym
from omegaconf import DictConfig
from math import sqrt
from copy import copy, deepcopy
from city import City

class TSP(gym.Env):
    """This class represents the TSP environment"""


    def __init__(self, config: DictConfig) -> None:
        self.file_path = config["data_file_path"]
        self.cities = load_data(self.file_path)
        self.cities_cache = deepcopy(self.cities)
        self.reward = 0
        self.obs = {}

    def reset(self):
        self.obs = {"non_visited_cities": self.cities_cache, "last_visited_city": City(0,0,0)}
        return self.obs

    def step(self, action: int):
        visited_city = self.cities[action]
        self.cities.pop(action)
        self.reward += sqrt(((self.obs["last_visited_city"].x_coord - visited_city.x_coord)**2)+((self.obs["last_visited_city"].y_coord - visited_city.y_coord) **2))
        if self.cities:
            self.obs = {"non_visited_cities": self.cities, "last_visited_city": visited_city}
            done = False
        else:
            self.obs = {}
            done = True

        return self.obs, self.reward, done

def load_data(file_path)-> list:
    lines = []
    with open(file_path) as f:
        lines = f.readlines()
    cities_list = [ line.split() for line in lines if line[0].isnumeric()]
    cities = [City(city[0], city[1], city[2]) for city in cities_list]

    return cities
