"""Global β-weighted federated averaging across clusters."""

from typing import List, Dict, Any


def global_aggregate(cluster_states: List[Dict[str, Any]], betas: List[float]) -> Dict[str, Any]:
    """Aggregate cluster models globally using β-weighted FedAvg."""
    if len(cluster_states) != len(betas):
        raise ValueError("cluster_states and betas must be the same length")

    total_beta = sum(betas)
    result: Dict[str, Any] = {}
    for key in cluster_states[0].keys():
        result[key] = sum(betas[i] * cluster_states[i][key] for i in range(len(cluster_states))) / total_beta
    return result
