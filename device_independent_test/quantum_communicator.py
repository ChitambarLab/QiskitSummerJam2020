from abc import ABC, abstractmethod
from qiskit import QuantumCircuit, execute

class QuantumDispatcher(ABC):
    # Abstract base class to define the functionality of a
    # ficitonal device which communicates states between quantum computers
    # Note that a future edit of this code may need to be able to specify which
    #       registers to transmit states between

    # @brief    Abstract method of running operations and
    #               transmitting resulting states
    # @params   pre_operation: operation to run before transmision
    #           post_operations: list of operations to run after transmission
    #           shot: number of shots to run
    # @Returns  Counts from running on all devices
    # @note     pre_operation is expected to be a single circuit on
    #               devices[0]. post_operations is a list of circuits on
    #               corresponding devices[i]
    @abstractmethod
    def run_and_transmit(self,pre_operation,post_operations,shot):
        pass

    # @brief    Abstract method of running batches of operations and
    #               transmitting resulting states
    # @params   pre_operations: array of operations to run before transmision
    #           post_operations: multidimensional array of operations to run after transmission
    #                            each column is an pair of operations to run
    #                            each element in the array is a list of operations for a single device
    # @Returns  Counts from running on all devices
    @abstractmethod
    def multi_run_and_transmit(self,pre_operations,post_operations,shot):
        pass

    # @brief    Abstract method of running all combinations of pre and post operations
    #           Runs all permutations of input operations, and output operations (permutes over all columns)
    # @params   pre_operations: array of all different operations to run before transmission
    #           post_operations: multidimensional array of all operations to run after transmission
    # @return   Counts from running on all devices
    @abstractmethod
    def batch_run_and_transmit(self,pre_operations,post_operations,shot):
        pass

class LocalDispatcher(QuantumDispatcher):
    # Concrete derived class from QuantumCommunicator
    # Runs circuits on a single computer
    # Note that input_registers and output_registers are not used

    def __init__(self,backend):
        self.devices = backend

    # @brief    Concatenates inputs to run a single circuit on a single computer
    # @params   pre_operation: operation to run before transmision
    #           post_operations: list of operations to run after transmission
    #           shot: number of shots to run
    # @returns  counts from running circuits or "NO MEASUREMENT" dictionary if
    #               there are no counts
    def run_and_transmit(self, pre_operations, post_operations, shots):
        # compose a single circuit from the input operations
        size = max(post_operations[0].num_qubits,post_operations[1].num_qubits)
        qc = QuantumCircuit(size)
        qc += pre_operations
        qc += post_operations[0] + post_operations[1]

        # run circuit on backend
        job = execute(qc, backend=self.devices[0], shots=shots)

        if job.result().data(qc) == {}:
            return {"NO_MEASUREMENT": 0}

        return job.result().get_counts(qc)

    # @brief    Method for running multiple circuits
    # @params   pre_operations: array of operations to run before transmision
    #           post_operations: multidimensional array of operations to run after transmission
    #                            each column is an pair of operations to run
    #                            each element in the array is a list of operations for a single device
    # @Returns  Counts from running on all devices
    def multi_run_and_transmit(self, pre_operations, post_operations, shots):
        # compose circuits from the input operations
        circuits = []
        for i in range (0,len(pre_operations)):
            qc = QuantumCircuit(max(post_operations[0][i].num_qubits,
                post_operations[1][i].num_qubits))
            qc += pre_operations[i]
            qc += post_operations[0][i] + post_operations[1][i]
            circuits.append(qc)
            display(qc.draw())

        # run circuit on backend
        job_set = execute(circuits, backend=self.devices[0], shots=shots)

        # retrieve and return counts
        counts = []
        for i in range (0,len(circuits)):
            if job_set.result().data(circuits[i]) != {}:
                counts.append(job_set.result().get_counts(circuits[i]))
            else:
                counts.append({"NO MEASUREMENT":0})
        return counts

    # @brief    Method for running all combinations of pre and post operations
    #           Runs all permutations of input operations, and output operations (permutes over all columns)
    # @params   pre_operations: array of all different operations to run before transmission
    #           post_operations: multidimensional array of all operations to run after transmission
    # @return   Counts from running on all devices
    def batch_run_and_transmit(self, pre_operations, post_operations, shots):
        pre_ops = []
        post_ops = [[],[]]

        # iterate over all combinations of operations
        for pre_operation in pre_operations:
            for post_op1 in post_operations[0]: # first list in post_operations array
                for post_op2 in post_operations[1]: # second list in post_operaitons array
                    pre_ops.append(pre_operation)
                    post_ops[0].append(post_op1)
                    post_ops[1].append(post_op2)

        return self.multi_run_and_transmit(pre_ops,post_ops,shots)
