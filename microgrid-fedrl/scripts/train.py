"""Entry point for training microgrid federated RL."""

from src.trainers.local_trainer import LocalTrainer
from src.safety.safetynet import SafetyNet
from src.utils.logger import Logger


def main():
    # TODO: load configs and initialize environment/agent
    logger = Logger()
    trainer = LocalTrainer(agent=None, env=None, safety=SafetyNet(), logger=logger)
    trainer.train()
    logger.close()


if __name__ == "__main__":
    main()
