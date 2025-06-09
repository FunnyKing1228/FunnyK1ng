"""Run validation and produce JSON and TensorBoard-style logs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.utils import load_yaml


class SummaryWriter:
    """Very small SummaryWriter compatible with this repository."""

    def __init__(self, log_dir: str | Path):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.file = (self.log_dir / "scalars.csv").open("w")
        self.file.write("tag,step,value\n")

    def add_scalar(self, tag: str, value: float, step: int) -> None:
        self.file.write(f"{tag},{step},{value}\n")

    def close(self) -> None:
        self.file.close()


def main(config_path: str, output_json: str, log_dir: str) -> None:
    cfg = load_yaml(config_path)

    writer = SummaryWriter(log_dir)
    results = {"average_reward": 0.0}
    episodes = int(cfg.get("eval_episodes", 5))

    for ep in range(episodes):
        # Placeholder reward generation
        reward = float(ep)
        writer.add_scalar("reward", reward, ep)
        results["average_reward"] += reward
    results["average_reward"] /= episodes
    writer.close()

    Path(output_json).parent.mkdir(parents=True, exist_ok=True)
    with open(output_json, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate federated RL")
    base = Path(__file__).resolve().parents[1]
    parser.add_argument("--config", default=str(base / "configs" / "hparams.yaml"))
    parser.add_argument("--out", default=str(base / "results" / "validate.json"))
    parser.add_argument("--logdir", default=str(base / "results" / "validate"))
    args = parser.parse_args()
    main(args.config, args.out, args.logdir)
