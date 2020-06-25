import unittest
import numpy as np

from device_independent_test import incompatible_measurement

class module_test_cases(unittest.TestCase):    
    def test_conditional_probs(self):
        shots = 1000
        counts = {
        	'1011': 78, '0000': 11, '0001': 103, '1001': 523, '1111': 17,
        	'1100': 14, '0101': 19, '1010': 16, '0111': 3, '1101': 103,
        	'0110': 1, '1110': 5, '1000': 91, '0011': 16
        }

        test_probs = incompatible_measurement.conditional_probs(counts, shots)
        match_probs = [[0.138,0.864,0.838,0.153],[0.862,0.136,0.162,0.847]]

        self.assertTrue(np.alltrue(test_probs == match_probs))

        shots = 10
        counts = {
        	'1000': 1, '0100': 2, '0010': 3, '0001': 4
        }

        test_probs = incompatible_measurement.conditional_probs(counts, shots)
        match_probs = [[.6,.7,.8,.9],[.4,.3,.2,0.1]]

        self.assertTrue(np.alltrue(test_probs == match_probs))