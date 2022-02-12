import hydra
from tsp import TSP
from random_agent import RandomAgent

from omegaconf import DictConfig

CONFIG_PATH = "./config"

@hydra.main(config_path=CONFIG_PATH, config_name="main")
def main(cfg: DictConfig) -> None:
    env = TSP(cfg)
    agent = RandomAgent(env)
    result = agent.run_episode()
    print(result)


if __name__ == '__main__':

    main()