import os
import datetime
from torch.utils.tensorboard import SummaryWriter


class Logger:
    """Thin wrapper around TensorBoard SummaryWriter."""

    def __init__(self, log_dir="results/runs", name="run"):
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        self.log_dir = os.path.join(log_dir, f"{name}_{timestamp}")
        os.makedirs(self.log_dir, exist_ok=True)
        self.writer = SummaryWriter(self.log_dir)

    def log_scalar(self, tag, value, step):
        """Log a scalar value."""
        self.writer.add_scalar(tag, value, step)

    def close(self):
        self.writer.close()
