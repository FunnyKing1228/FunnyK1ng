import json
import math
import os


class SafetyNet:
    """Simple logistic regression safety model."""

    def __init__(self, model_path=None):
        if model_path is None:
            model_path = os.path.join(os.path.dirname(__file__), 'safety_model.pt')
        self.model = None
        if os.path.exists(model_path):
            with open(model_path, 'r') as f:
                self.model = json.load(f)
        else:
            self.model = {'w': [0.0, 0.0], 'b': 0.0}

    def _sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    def is_safe(self, state, action):
        """Return True if action is considered safe for given state."""
        z = (
            self.model['w'][0] * float(state)
            + self.model['w'][1] * float(action)
            + self.model['b']
        )
        p = self._sigmoid(z)
        return p >= 0.5

    def is_safe_batch(self, states, actions):
        return [self.is_safe(s, a) for s, a in zip(states, actions)]
