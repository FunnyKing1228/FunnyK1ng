from __future__ import annotations
import random
from typing import List, Dict, Any


LOAD_TYPES = ["residential", "commercial", "industrial"]
STORAGE_TYPES = ["battery", "flywheel"]


class MicrogridEnv:
    """Simplified microgrid environment with load and storage modules."""

    def __init__(self, loads: List[Dict[str, Any]] | None = None,
                 storages: List[Dict[str, Any]] | None = None,
                 horizon: int = 24):
        self.loads = loads or []
        self.storages = storages or []
        self.horizon = horizon
        self.time = 0
        self.storage_levels = [s.get("capacity", 0) for s in self.storages]

    def reset(self) -> Dict[str, Any]:
        self.time = 0
        self.storage_levels = [s.get("capacity", 0) for s in self.storages]
        return self._get_state()

    def step(self, action: Any) -> tuple[Dict[str, Any], float, bool, Dict[str, Any]]:
        # Placeholder dynamics: advance time and return negative total demand as reward
        self.time += 1
        demand = sum(load.get("profile", [0]*self.horizon)[self.time-1]
                      if self.time-1 < len(load.get("profile", [])) else 0
                      for load in self.loads)
        reward = -demand
        done = self.time >= self.horizon
        return self._get_state(), reward, done, {}

    def _get_state(self) -> Dict[str, Any]:
        return {
            "time": self.time,
            "storage_levels": list(self.storage_levels),
        }


def random_load() -> Dict[str, Any]:
    load_type = random.choice(LOAD_TYPES)
    profile = [round(random.uniform(0.5, 1.5), 2) for _ in range(24)]
    return {"type": load_type, "profile": profile}


def random_storage() -> Dict[str, Any]:
    storage_type = random.choice(STORAGE_TYPES)
    capacity = random.randint(50, 200)
    return {"type": storage_type, "capacity": capacity}
