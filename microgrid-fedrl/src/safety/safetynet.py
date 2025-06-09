class SafetyNet:
    """Placeholder SafetyNet model."""

    def __init__(self, model=None):
        self.model = model

    def is_safe(self, state, action):
        """Return True if action is considered safe for given state."""
        # TODO: implement real safety model
        return True

    def is_safe_batch(self, states, actions):
        return [self.is_safe(s, a) for s, a in zip(states, actions)]
