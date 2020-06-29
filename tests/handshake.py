import unittest
from qiskit import IBMQ
from device_independent_test import quantum_communicator
from device_independent_test import handshake

class module_test_cases(unittest.TestCase):
    def incompatible_measurement(self):
        provider = IBMQ.load_account()
        communicator = quantum_communicator.LocalDispatcher([provider.get_backend('ibmq_qasm_simulator')])
        obj = HandShake(communicator)
        try:
            obj.measurement_incompatibility(0.0,1000)
        except:
            print("Measurment incompatibility does not run.")
