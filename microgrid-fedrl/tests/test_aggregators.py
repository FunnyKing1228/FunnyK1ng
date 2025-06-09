import os
import sys
import math

# Add project root (microgrid-fedrl) to sys.path so `src` package can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.trainers.cluster import cluster_aggregate
import importlib

global_module = importlib.import_module('src.trainers.global')
global_aggregate = global_module.global_aggregate


def test_cluster_beta_fedavg():
    states = [
        {'w': 1.0},
        {'w': 2.0},
        {'w': 3.0},
    ]
    betas = [0.2, 0.3, 0.5]
    result = cluster_aggregate(states, betas)
    assert math.isclose(result['w'], 2.3)


def test_global_beta_fedavg():
    cluster_states = [
        {'w': 2.3},
        {'w': 1.0},
        {'w': 3.0},
    ]
    betas = [0.5, 0.2, 0.3]
    result = global_aggregate(cluster_states, betas)
    assert math.isclose(result['w'], 2.25)
