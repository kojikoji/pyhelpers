import unittest
import numpy as np
from pyhelpers import helpers


class TestFUncs(unittest.TestCase):
    def test_make_disc(self):
        vec = np.arange(10)
        disc_vec = helpers.make_disc(vec, 3)
        self.assertAlmostEqual(disc_vec[9], 2)


if __name__ == '__main__':
    unittest.main()
