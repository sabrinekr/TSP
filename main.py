import hydra
from tsp import TSP

from omegaconf import DictConfig

CONFIG_PATH = "./config"

@hydra.main(config_path=CONFIG_PATH, config_name="main")
def main(cfg: DictConfig) -> None:
    env = TSP(cfg)


if __name__ == '__main__':

    main()