import random
import numpy as np

class RandomAgent():
    """interface of general agents"""

    def __init__(self, env):
        self.env = env
        np.random.seed(1234)

    def compute_action(self, observation):
        action = random.randint(0, len(observation["non_visited_cities"])-1)
        return action

    def run_episode(self):
        obs = self.env.reset()
        done = False
        obs_list = []
        while not done:
            action = self.compute_action(obs)
            new_obs, reward, done = self.env.step(action)
            obs = new_obs
            obs_list.append(action)
        return reward

