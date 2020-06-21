import unittest
import numpy as np
from qiskit.quantum_info import Statevector

from module import example

class module_test_cases(unittest.TestCase):
    def test_hello(self):
        example.hello()
        pass
    
    def test_add_two(self):
        self.assertEqual(4, example.add_two(2))
        self.assertEqual(7, example.add_two(5))

    def test_parabola(self):
        self.assertEqual(
            [9,4,1,0,1,4], list( map(
                example.parabola,  np.arange(-3,3)
            ))
        )

    def test_prepare_01_circuit(self):
        circ = example.prepare_01_circuit()
        state = Statevector.from_instruction(circ)
        
        self.assertEqual(
            list(state.data), [0,0,1,0]
        )