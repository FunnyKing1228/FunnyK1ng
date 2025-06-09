# Safety-Enhanced Hierarchical Federated RL Microgrid

This repository contains a skeleton implementation inspired by the design
outlined for a Safety-Enhanced Hierarchical Federated Reinforcement Learning
framework. The project structure mirrors the proposed layout and provides
placeholder modules for future development.

## Directory Layout

```
microgrid-fedrl/
├── configs/            # YAML configs for environments and experiments
│   ├── clients/
│   ├── clusters.yaml
│   └── hparams.yaml
├── data/               # generated time-series or datasets
├── src/
│   ├── envs/           # environment wrappers
│   ├── safety/         # SafetyNet model
│   ├── agents/         # RL agents and federated interfaces
│   ├── trainers/       # trainers and aggregators
│   └── utils/          # common utilities
├── scripts/            # CLI for training/evaluation
└── results/            # tensorboard logs and checkpoints
```

The code currently provides minimal placeholders for key components such as
`SafetyNet`, `LocalTrainer`, and a simple `fed_avg` aggregator. Further
implementation is required to realize the full functionality described in the
project blueprint.

## Environment and Scenario Generation

The `src/envs` package contains a simple `MicrogridEnv` class along with a
`make_random_scenario` helper which generates YAML configuration files for a set
of clients. By default it produces 9 client files under a specified directory.
Each scenario randomly samples from three load types (`residential`,
`commercial`, `industrial`) and two storage types (`battery`, `flywheel`).

### Installation

Install the package in editable mode using pip:

```bash
pip install -e .
```

## Logging and Analysis

Training scripts now integrate a simple `Logger` utility based on
TensorBoard. Logs are stored under `microgrid-fedrl/results/runs` and can be
visualized using TensorBoard or the Jupyter notebook found at
`analysis/plot_results.ipynb`.
