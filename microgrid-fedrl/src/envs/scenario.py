from __future__ import annotations
import random
from pathlib import Path
from typing import List, Dict, Any
import yaml

from .microgrid_env import random_load, random_storage


def make_random_scenario(out_dir: str | Path,
                         num_clients: int = 9,
                         seed: int | None = None) -> List[Dict[str, Any]]:
    """Generate random scenarios for multiple clients and export YAML files."""
    rng = random.Random(seed)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    scenarios = []
    for i in range(num_clients):
        n_loads = rng.randint(1, 3)
        n_storages = rng.randint(1, 2)
        loads = [random_load() for _ in range(n_loads)]
        storages = [random_storage() for _ in range(n_storages)]
        scenario = {
            "modules": {
                "loads": loads,
                "storages": storages,
            },
            "time_series": [],
        }
        scenarios.append(scenario)
        with open(out_path / f"client_{i}.yaml", "w") as f:
            yaml.safe_dump(scenario, f)
    return scenarios
