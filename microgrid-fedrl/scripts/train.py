"""Entry point for training microgrid federated RL."""

from src.trainers.local_trainer import LocalTrainer
from src.safety.safetynet import SafetyNet


def main():
    # TODO: load configs and initialize environment/agent
    trainer = LocalTrainer(agent=None, env=None, safety=SafetyNet())
    trainer.train()


if __name__ == "__main__":
    main()
