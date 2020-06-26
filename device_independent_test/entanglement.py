import numpy as np
from qiskit import IBMQ, QuantumCircuit, execute
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq.managed import IBMQJobManager

class EntanglementTest:
    @staticmethod
    def create_bell_state():
        """Creates two qubit bell state

        Returns:
            QuantumCircuit: created circuit
        """
        circuit = QuantumCircuit(2)
        circuit.h(0)
        circuit.cx(0,1)
        return circuit

    @staticmethod
    def compute_expectation_for_CHSH(counts, shots):
        return (counts["00"] + counts["11"] - counts["01"] - counts["10"])/shots

    def __init__(self):
        self.provider = IBMQ.load_account()
        self.job_set = None

    def run_CHSH_test(self, backend="ibmq_qasm_simulator", shots=1000):
        qc1 = self.measure_in_ZW()
        qc2 = self.measure_in_ZV()
        qc3 = self.measure_in_XW()
        qc4 = self.measure_in_XV()

        self.run_jobs([qc1, qc2, qc3, qc4], backend, shots, name="CHSH")
        
        results = self.job_set.results()
        expected_ZW = self.compute_expectation_for_CHSH(results.get_counts(0), shots)
        expected_ZV = self.compute_expectation_for_CHSH(results.get_counts(1), shots)
        expected_XW = self.compute_expectation_for_CHSH(results.get_counts(2), shots)
        expected_XV = self.compute_expectation_for_CHSH(results.get_counts(3), shots)

        return {
            "received": (expected_ZW + expected_ZV + expected_XW - expected_XV),
            "expected": 2*np.sqrt(2)
        }

    def measure_in_ZW(self):
        circuit = self.create_bell_state()
        circuit.s(1)
        circuit.h(1)
        circuit.t(1)
        circuit.h(1)
        circuit.measure_all()
        return circuit

    def measure_in_ZV(self):
        circuit = self.create_bell_state()
        circuit.s(1)
        circuit.h(1)
        circuit.tdg(1)
        circuit.h(1)
        circuit.measure_all()
        return circuit

    def measure_in_XW(self):
        circuit = self.create_bell_state()
        circuit.h(0)
        circuit.s(1)
        circuit.h(1)
        circuit.t(1)
        circuit.h(1)
        circuit.measure_all()
        return circuit

    def measure_in_XV(self):
        circuit = self.create_bell_state()
        circuit.h(0)
        circuit.s(1)
        circuit.h(1)
        circuit.tdg(1)
        circuit.h(1)
        circuit.measure_all()
        return circuit

    def run_jobs(self, circuits, backend, shots, name):
        """Run jobs using IBMQJobManager

        Args:
            circuits ([QuantumCircuit]): circuits to run
            backend (string): device name
            shots (int, optional): number of shots

        Returns:
            ManagedJobSet: set of jobs to be executed
        """
        job_manager = IBMQJobManager()
        self.job_set = job_manager.run(
            circuits,
            backend=self.provider.get_backend(backend),
            shots=shots,
            name=name
        )
        self.job_set.error_messages()

