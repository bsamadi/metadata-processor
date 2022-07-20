import unittest
from app.sun_pos import sun_pos
from app.is_glare import is_glare


class AnglesTest(unittest.TestCase):
    def test_is_glare(self):
        payload = {
            "lat": 49.2699648,
            "lon": -123.1290368,
            "epoch": 1588704959.321,
            "orientation": -10.2,
        }

        # Calculate the position of the sun
        sun = sun_pos(payload)

        self.assertEqual(
            is_glare(sun, payload["orientation"]), "false",
            msg="glare should be false",
        )
