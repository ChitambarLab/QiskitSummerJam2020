import numpy as np
from qiskit import IBMQ, QuantumCircuit, execute

# @brief    Circuit creating the + bell state
# @returns  Two qubit circuit resulting in the + bell state
def create_bell_state():
    """Creates two qubit bell state

    Returns:
    QuantumCircuit: created circuit
    """
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0,1)
    return circuit

# @brief    Computes the CHSH expecation value from a job
# @params   counts: dictionary of measurements
#           shots:  number of shots
# @returns  float expectation value
def compute_expectation_for_CHSH(counts, shots):
    return (counts["00"] + counts["11"] - counts["01"] - counts["10"])/shots

# @brief    Runs a CHSH test
# @params   dispatcher: QuantumDispatcher to run circuits and transmit states
#           tolerance: max deviation from quantum expectation value allowed
#           shots: number of shots to run
def run_test(dispatcher,tolerance=0.4,shots=1000):
    pre_ops = [create_bell_state()]
    post_ops = [[QuantumCircuit(2)],[measure_in_ZW(),measure_in_ZV(),measure_in_XW(),measure_in_XV()]]

    # run all permutations through the dispatcher
    counts = dispatcher.batch_run_and_transmit(pre_ops,post_ops,shots)
    expected_ZW = compute_expectation_for_CHSH(counts[0], shots)
    expected_ZV = compute_expectation_for_CHSH(counts[1], shots)
    expected_XW = compute_expectation_for_CHSH(counts[2], shots)
    expected_XV = compute_expectation_for_CHSH(counts[3], shots)

    test_val = (expected_ZW + expected_ZV + expected_XW - expected_XV)
    expectation_value = 2.82842712475 # quantum expectation value

    return (abs(test_val-expectation_value) <= tolerance, test_val)

# @brief    Circuit for Alice measuring in Z basis, Bob measuring in Hadamard basis
# @returns  Two qubit circuit with a Hadamard basis projective measurment on the first register,
#               Z projective measurment on the second
def measure_in_ZW():
    circuit = QuantumCircuit(2)
    circuit.s(1)
    circuit.h(1)
    circuit.t(1)
    circuit.h(1)
    circuit.measure_all()
    return circuit

# @brief    Circuit for Alice measuring in Z basis, Bob measuring in (Z-X) basis
# @returns  Two qubit circuit with a (Z-X) basis projective measurment on the first register,
#               Z projective measurment on the second
def measure_in_ZV():
    circuit = QuantumCircuit(2)
    circuit.s(1)
    circuit.h(1)
    circuit.tdg(1)
    circuit.h(1)
    circuit.measure_all()
    return circuit

# @brief    Circuit for Alice measuring in X basis, Bob measuring in Hadamard basis
# @returns  Two qubit circuit with a Hadamard projective measurment on the first register,
#               X projective measurment on the second
def measure_in_XW():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.s(1)
    circuit.h(1)
    circuit.t(1)
    circuit.h(1)
    circuit.measure_all()
    return circuit

# @brief    Circuit for Alice measuring in X basis, Bob measuring in (Z-X)d basis
# @returns  Two qubit circuit with a (Z-X) basis projective measurment on the first register,
#               Z projective measurment on the second
def measure_in_XV():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.s(1)
    circuit.h(1)
    circuit.tdg(1)
    circuit.h(1)
    circuit.measure_all()
    return circuit
