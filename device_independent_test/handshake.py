from . import quantum_communicator
from . import incompatible_measurement
from . import new_entanglement

class HandShake():

    def __init__(self,communicator: quantum_communicator.QuantumDispatcher):
        self.dispatcher = communicator

    def dimensionality(self,tolerance,shots):
        pass
    def measurement_incompatibility(self,tolerance,shots):
        result = incompatible_measurement.run_test(self.dispatcher,tolerance,shots)
        if result[0]:
            print("Passed Measurment Incompatibility with violation: ", result[1])
        else:
            print("Failed Measurment Incompatibility with violation: ", result[1])
        return result
    def entanglement(self,tolerance,shots):
        result = new_entanglement.run_test(self.dispatcher,tolerance,shots)
        if result[0]:
            print("Passed Entanglement with violation: ", result[1])
        else:
            print("Failed Entanglement with violation: ", result[1])
        return result
    def test_all(self,tolerance,shots):
        pass

    def test(self,name,tolerance,shots):
        try:
            getattr(self,name)(tolerance,shots)
        except:
            print("Test not found.")
            self.print_tests()

    def print_tests(self):
        print("dimensionality, measurement_incompatibility, entanglement, and test_all")

    def write_to(self,file):
        pass
