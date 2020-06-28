from device_independent_test import quantum_communicator
from device_independent_test import incompatible_measurement
from device_independent_test import entanglement

class HandShake():
    # Object interface between the user and the test modules
    # Stores a dispatcher to send to modules
    # Runs both individual and sets of tests

    def __init__(self,communicator: quantum_communicator.QuantumDispatcher):
        self.dispatcher = communicator

    # Run dimenionality test
    def dimensionality(self,tolerance,shots):
        pass

    # Run measurement incompatibility test
    def measurement_incompatibility(self,tolerance,shots):
        result = incompatible_measurement.run_test(self.dispatcher,tolerance,shots)
        if result[0]:
            print("Passed Measurment Incompatibility with value: ", result[1])
        else:
            print("Failed Measurment Incompatibility with value: ", result[1])
        return result

    # Run entanglement test
    def entanglement(self,tolerance,shots):
        result = entanglement.run_test(self.dispatcher,tolerance,shots)
        if result[0]:
            print("Passed Entanglement with value: ", result[1])
        else:
            print("Failed Entanglement with value: ", result[1])
        return result

    # Run all tests to verify functioning computer/connection
    def test_all(self,tolerance,shots):
        pass

    def print_tests(self):
        print("dimensionality, measurement_incompatibility, entanglement, and test_all")

    # To do? Write stored data/analysis to a file
    def write_to(self,file):
        pass
