class LocalTrainer:
    """Simplified local training loop placeholder."""

    LOCAL_EPISODES = 20

    def __init__(self, agent, env, safety, logger=None):
        self.agent = agent
        self.env = env
        self.safety = safety
        self.logger = logger

    def train(self):
        for ep in range(self.LOCAL_EPISODES):
            state = self.env.reset()
            done = False
            episode_reward = 0
            violations = 0
            steps = 0
            while not done:
                q_values = self.agent(state)
                # TODO: compute available actions and mask using safety
                action = q_values.argmax()
                if not self.safety.is_safe(state, action):
                    violations += 1
                state, reward, done, info = self.env.step(action)
                episode_reward += reward
                steps += 1
                # TODO: update agent
            if self.logger:
                self.logger.log_scalar("episode_reward", episode_reward, ep)
                if steps:
                    violation_rate = violations / steps
                    self.logger.log_scalar("violation_rate", violation_rate, ep)
