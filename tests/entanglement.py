import unittest

import numpy as np
from qiskit.quantum_info import Statevector

from device_independent_test import entanglement

class module_test_cases(unittest.TestCase):
	def test_EntanglmentTest(self):
		test = entanglement.EntanglementTest()
		qc = test.create_bell_state()

		test_state = Statevector.from_instruction(qc)

		self.assertAlmostEqual(test_state.data[0], 1/np.sqrt(2))
		self.assertAlmostEqual(test_state.data[1], 0)
		self.assertAlmostEqual(test_state.data[2], 0)
		self.assertAlmostEqual(test_state.data[3], 1/np.sqrt(2))