from device_independent_test import dimension
from device_independent_test import entanglement
from device_independent_test import incompatible_measurement
from device_independent_test import quantum_communicator

class HandShake():
    # Object interface between the user and the test modules
    # Stores a dispatcher to send to modules
    # Runs both individual and sets of tests

    def __init__(self, communicator: quantum_communicator.QuantumDispatcher):
        self.dispatcher = communicator

    # Run dimenionality test
    def dimensionality(self, tolerance, shots):
        (passed, value) = dimension.run_test(self.dispatcher, tolerance, shots)
        if passed:
            print("Passed Dimensionality with value: ", value)
        else:
            print("Failed Dimensionality with value: ", value)
        return (passed, value)

    # Run measurement incompatibility test
    def measurement_incompatibility(self, tolerance, shots, parallel=1):
        if parallel:
            (passed,value) = incompatible_measurement.run_test_parallel(self.dispatcher, tolerance, shots)
        else:
            (passed,value) = incompatible_measurement.run_test(self.dispatcher, tolerance, shots)
        if passed:
            print("Passed Measurment Incompatibility with value: ", value)
        else:
            print("Failed Measurment Incompatibility with value: ", value)
        return (passed, value)

    # Run entanglement test
    def entanglement(self, tolerance, shots, parallel=1):
        if parallel:
            (passed, value) = entanglement.run_test_parallel(self.dispatcher, tolerance, shots)
        else:
            (passed, value) = entanglement.run_test(self.dispatcher, tolerance, shots)
        if passed:
            print("Passed Entanglement with value: ", value)
        else:
            print("Failed Entanglement with value: ", value)
        return (passed, value)

    # Run all tests to verify functioning computer/connection
    def test_all(self, tolerance, shots):
        dimensionality = self.dimensionality(tolerance, shots)
        measurement_incompatiblility = self.measurement_incompatibility(tolerance, shots)
        entanglement = self.entanglement(tolerance, shots)

        if dimensionality[0] & measurement_incompatiblility[0] & entanglement[0]:
            return True
        else:
            return False

    def print_tests(self):
        print("dimensionality, measurement_incompatibility, entanglement, and test_all")

    # To do? Write stored data/analysis to a file
    def write_to(self,file):
        pass
