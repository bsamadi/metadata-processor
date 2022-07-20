import unittest

import numpy as np
from numpy import pi

class AnglesTest(unittest.TestCase):

    def test_clipping_upper_bounds(self):
        angles = [0, 10, 10, 10, 10, 10, 10]
        clipped_angels = get_clipped_state(angles)

        for angle in clipped_angels:
            self.assertTrue(angle < 10, msg='angle should have been clipped to something smaller')
