import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from safety.safetynet import SafetyNet


class TestSafetyNet(unittest.TestCase):
    def setUp(self):
        model_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'safety', 'safety_model.pt')
        self.net = SafetyNet(model_path=model_path)

    def test_is_safe(self):
        # Cases from training data
        self.assertTrue(self.net.is_safe(0.3, 0.9))
        self.assertFalse(self.net.is_safe(0.2, 0.1))
        self.assertTrue(self.net.is_safe(0.9, 0.5))
        self.assertFalse(self.net.is_safe(0.4, 0.2))

    def test_batch(self):
        states = [0.3, 0.2, 0.9, 0.4]
        actions = [0.9, 0.1, 0.5, 0.2]
        expected = [True, False, True, False]
        self.assertEqual(self.net.is_safe_batch(states, actions), expected)


if __name__ == '__main__':
    unittest.main()
