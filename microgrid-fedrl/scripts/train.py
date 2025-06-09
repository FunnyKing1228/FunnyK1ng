"""Entry point for training microgrid federated RL."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow running without installing the package
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.safety.safetynet import SafetyNet
from src.trainers.local_trainer import LocalTrainer
from src.utils import load_yaml


def main(config_path: str) -> None:
    """Load config from ``config_path`` and run training."""
    cfg = load_yaml(config_path)
    episodes = int(cfg.get("local_episodes", LocalTrainer.LOCAL_EPISODES))
    trainer = LocalTrainer(
        agent=None,
        env=None,
        safety=SafetyNet(),
        episodes=episodes,
    )
    print(f"Loaded config: {cfg}")
    if trainer.agent is not None and trainer.env is not None:
        trainer.train()
    else:
        print("Agent or environment not configured; skipping training loop.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train federated RL")
    default_cfg = Path(__file__).resolve().parents[1] / "configs" / "hparams.yaml"
    parser.add_argument(
        "--config", default=str(default_cfg), help="Path to YAML config"
    )
    args = parser.parse_args()
    main(args.config)
