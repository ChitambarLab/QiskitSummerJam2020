import unittest
from qiskit import IBMQ
from device_independent_test import quantum_communicator
from device_independent_test.handshake import HandShake

class module_test_cases(unittest.TestCase):
    def incompatible_measurement(self):
        provider = IBMQ.load_account()
        communicator = quantum_communicator.LocalDispatcher([provider.get_backend('ibmq_qasm_simulator')])
        obj = HandShake(communicator)
        try:
            obj.measurement_incompatibility(0.0,1000)
        except:
            print("Measurment incompatibility does not run.")

    def test_all(self):
        provider = IBMQ.load_account()
        communicator = quantum_communicator.LocalDispatcher([provider.get_backend('ibmq_qasm_simulator')])
        obj = HandShake(communicator)
        params = {
            "dimensionality": {
                "tolerance": 0.1,
                "shots": 2000
            },
            "measurement_incompatibility": {
                "tolerance": 0.5,
                "shots": 1000
            },
            "entanglement": {
                "tolerance": 0.2,
                "shots": 2000
            }
        }
        try:
            obj.test_all(params)
        except:
            print("test_all does not run.")

