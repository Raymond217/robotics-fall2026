import os
import unittest
from week03_pattern.pattern import build_pattern

class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        #rounded rectangle should have eight segments:
        self.assertEqual(len(segments),8)
        #first segment moves forward with no rotation
        self.assertGreater(segments[0].linear_x,0.0)
        self.assertEqual(segments[0].angular_z,0.0)
        #Turning segments should turn left
        self.assertGreater(segments[1].angular_z,0.0)
        self.assertGreater(segments[3].angular_z,0.0)
        self.assertGreater(segments[5].angular_z,0.0)
        self.assertGreater(segments[7].angular_z,0.0)
    def test_my_pattern_order(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])
        #The pattern alternates straight and turning segments
        self.assertEqual(segments[0].angular_z,0.0)
        self.assertNotEqual(segments[1].angular_z,0.0)

        self.assertEqual(segments[2].angular_z,0.0)
        self.assertNotEqual(segments[3].angular_z,0.0)

        self.assertEqual(segments[4].angular_z,0.0)
        self.assertNotEqual(segments[5].angular_z,0.0)
   
        self.assertEqual(segments[6].angular_z,0.0)
        self.assertNotEqual(segments[7].angular_z,0.0)


if __name__ == "__main__":
   unittest.main()
