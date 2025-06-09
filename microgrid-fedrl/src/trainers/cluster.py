"""Cluster-level β-weighted federated averaging."""

from typing import List, Dict, Any


def cluster_aggregate(states: List[Dict[str, Any]], betas: List[float]) -> Dict[str, Any]:
    """Aggregate client states within a cluster using β-weighted FedAvg.

    Parameters
    ----------
    states : list of dict
        Model parameter dictionaries from each client.
    betas : list of float
        Weight for each client. Must have same length as ``states``.

    Returns
    -------
    dict
        Aggregated model parameters.
    """
    if len(states) != len(betas):
        raise ValueError("states and betas must be the same length")

    total_beta = sum(betas)
    result: Dict[str, Any] = {}
    for key in states[0].keys():
        result[key] = sum(betas[i] * states[i][key] for i in range(len(states))) / total_beta
    return result
