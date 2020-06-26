from abc import ABC, abstractmethod
from qiskit import QuantumCircuit, execute
from qiskit.providers.ibmq.managed import IBMQJobManager

class QuantumCommunicator(ABC):
    # Abstract base class to define the functionality of a
    # ficitonal device which communicates states between quantum computers

    # @brief    Constructor taking in two backends
    # @params   backends: array of devices to run on
    def __init__(self, backends):
        self.devices = backends

    # @brief    Abstract method of running operations and
    #               transmitting resulting states
    # @params   input_registers: registers to transmit states from
    #           output_registers: registers to transmit states to
    #           pre_operations: operations to run before transmision
    #           post_operations: tuple of operations to run after transmission
    #           shot: number of shots to run
    # @Returns  Counts from running on all devices
    # @note     pre_operations is expected to be a single circuit
    #               for Alice's device. post_operations is a tuple
    #               of form (alice's circuit, bob's circuit)
    @abstractmethod
    def run_and_transmit(self,input_registers,output_registers,pre_operations,post_operations,shot):
        pass

    # @brief    Abstract method of running batches of operations and
    #               transmitting resulting states
    # @params   input_registers: registers to transmit states from
    #           output_registers: registers to transmit states to
    #           pre_operations: array of operations to run before transmision
    #           post_operations: array of tuples of operations to run after transmission
    # @Returns  Counts from running on all devices
    # @note     pre_operations is expected to be a single circuit
    #               for Alice's device. post_operations is a tuple
    #               of form (alice's circuit, bob's circuit)
    #           Shots are fixed at 1000 per circuit
    @abstractmethod
    def multi_run_and_transmit(self,input_registers,output_registers,pre_operations,post_operations):
        pass

    # @brief    Abstract method of running all combinations of pre and post operations
    # @params   input_registers: registers to transmit states from
    #           output_registers: registers to transmit states to
    #           pre_operations: array of all different operations to run before transmission
    #           post_operations: multidimensional array of all operations to run after transmission
    # @return   Counts from running on all devices
    # @note     Shots are fixed at 1000 per circuit
    @abstractmethod
    def batch_run_and_transmit(self,input_register,output_registers,pre_operations,post_operations):
        pass

    # Mutator for array of devices
    def set_devices(self,new_backends):
        self.devices = new_backends


class LocalCommunicator(QuantumCommunicator):
    # Concrete derived class from QuantumCommunicator
    # Runs circuits on a single computer

    def __init__(self,backend):
        self.devices = backend

    def run_and_transmit(self,input_registers,output_registers,pre_operations,post_operations,shot):
        # simply compose a single circuit from the input operations
        size = max(post_operations[0].num_qubits,post_operations[1].num_qubits)
        qc = QuantumCircuit(size)
        qc += pre_operations
        qc += post_operations[0] + post_operations[1]

        # run circuit on backend
        job = execute(qc, backend=self.devices[0], shots=shot)
        return job.result().get_counts(qc)

    def multi_run_and_transmit(self,input_registers,output_registers,pre_operations,post_operations):
        # simply compose circuits from the input operations
        circuits = []
        for i in range (0,len(pre_operations)):
            qc = QuantumCircuit(max(post_operations[i][0].num_qubits(),
                post_operations[i][1].num_qubits()))
            qc += pre_operations[i]
            qc += post_operations[i][0] + post_operations[i][1]
            circuits.append(qc)

        # run circuit on backend
        job_manager = IBMQJobManager()
        job_set = job_manager.run(qc, backend=self.devices[0], name='msrincom_test')
        job_set.error_messages()

        # retrieve and return counts
        counts = job_set.results().get_counts(0:len(pre_operations))
        return counts
