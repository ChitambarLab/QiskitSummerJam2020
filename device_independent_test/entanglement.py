import numpy as np
from qiskit import IBMQ, QuantumCircuit, execute

def create_bell_state():
      """Creates two qubit bell state

      Returns:
          QuantumCircuit: created circuit
      """
      circuit = QuantumCircuit(2)
      circuit.h(0)
      circuit.cx(0,1)
      return circuit

def compute_expectation_for_CHSH(counts, shots):
      return (counts["00"] + counts["11"] - counts["01"] - counts["10"])/shots

def run_test(dispatcher,tolerance=0.0,shots=1000):
        pre_ops = [create_bell_state()]
        post_ops = [[QuantumCircuit(2)],[measure_in_ZW(),measure_in_ZV(),measure_in_XW(),measure_in_XV()]]

        counts = dispatcher.batch_run_and_transmit([0,1],[0,1],pre_ops,post_ops,shots)
        expected_ZW = compute_expectation_for_CHSH(counts[0], shots)
        expected_ZV = compute_expectation_for_CHSH(counts[1], shots)
        expected_XW = compute_expectation_for_CHSH(counts[2], shots)
        expected_XV = compute_expectation_for_CHSH(counts[3], shots)

        test_val = (expected_ZW + expected_ZV + expected_XW - expected_XV)
        classical_val = 2

        return (test_val > classical_val + tolerance,test_val)

def measure_in_ZW():
    circuit = QuantumCircuit(2)
    circuit.s(1)
    circuit.h(1)
    circuit.t(1)
    circuit.h(1)
    circuit.measure_all()
    return circuit

def measure_in_ZV():
         circuit = QuantumCircuit(2)
         circuit.s(1)
         circuit.h(1)
         circuit.tdg(1)
         circuit.h(1)
         circuit.measure_all()
         return circuit

def measure_in_XW():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.s(1)
    circuit.h(1)
    circuit.t(1)
    circuit.h(1)
    circuit.measure_all()
    return circuit

def measure_in_XV():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.s(1)
    circuit.h(1)
    circuit.tdg(1)
    circuit.h(1)
    circuit.measure_all()
    return circuit
