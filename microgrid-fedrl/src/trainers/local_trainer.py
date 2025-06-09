class LocalTrainer:
    """Simplified local training loop placeholder."""

    LOCAL_EPISODES = 20

    def __init__(self, agent, env, safety):
        self.agent = agent
        self.env = env
        self.safety = safety

    def train(self):
        for ep in range(self.LOCAL_EPISODES):
            state = self.env.reset()
            done = False
            while not done:
                q_values = self.agent(state)
                # TODO: compute available actions and mask using safety
                action = q_values.argmax()
                state, reward, done, info = self.env.step(action)
                # TODO: update agent
