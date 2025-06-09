class LocalTrainer:
    """Simplified local training loop placeholder."""

    LOCAL_EPISODES = 20

    def __init__(self, agent, env, safety, episodes: int | None = None):
        self.agent = agent
        self.env = env
        self.safety = safety
        self.local_episodes = episodes if episodes is not None else self.LOCAL_EPISODES

    def train(self):
        for ep in range(self.local_episodes):
            state = self.env.reset()
            done = False
            while not done:
                q_values = self.agent(state)
                # TODO: compute available actions and mask using safety
                action = q_values.argmax()
                state, reward, done, info = self.env.step(action)
                # TODO: update agent
