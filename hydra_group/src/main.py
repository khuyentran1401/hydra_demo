import hydra
from omegaconf import DictConfig
from process_data import process_data
from segment import segment


@hydra.main(config_path="../config", config_name="main")
def main(config: DictConfig):

    if config.flow == "all":
        process_data(config)
        segment(config)

    elif config.flow == "process_data":
        process_data(config)

    elif config.flow == "segment":
        segment(config)

    else:
        print("flow not found")


if __name__ == "__main__":
    main()
