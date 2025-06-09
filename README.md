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

### SafetyNet Training

Sample labelled data for the SafetyNet model lives under `microgrid-fedrl/data/safetynet/train.csv`.
Run the training script below to produce `safety_model.pt` which is loaded by
`SafetyNet.is_safe`:

```bash
python3 microgrid-fedrl/src/safety/train.py
```

Unit tests in `microgrid-fedrl/tests/` validate the behaviour of the API.
