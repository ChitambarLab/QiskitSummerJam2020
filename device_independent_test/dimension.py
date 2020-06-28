from qiskit import QuantumCircuit

def run_test(dispatcher, tolerance, shots):
    """Runs dimensionality test for 2-qubits system. Alice prepares all possible
    orthogonal states (no rotation), and Bob measures in corresponding canonical
    states.

    Args:
        dispatcher (QuantumDispatcher)
        tolerance (Number): passing tolerance
        shots (int): number of shots to run

    Returns:
        Boolean: True if pass, False if fail
    """
    initial_states = [[0, 0], [0, 1], [1, 0], [1, 1]]
    pre_ops = []

    for state in initial_states:
        pre_ops.append(prepare_bit_circuit(state))

    post_ops = [[QuantumCircuit(2)], [measure_circuit()]]
    
    counts = dispatcher.batch_run_and_transmit(pre_ops, post_ops, shots)

    success_prob = compute_success_probability(counts, shots)
    passed = 1. - tolerance <= success_prob <= 1. + tolerance
    return (passed, success_prob)

def compute_success_probability(counts, shots):
    count_00 = counts[0]["00"] if "00" in counts[0] else 0
    count_01 = counts[1]["10"] if "10" in counts[1] else 0
    count_10 = counts[2]["01"] if "01" in counts[2] else 0
    count_11 = counts[3]["11"] if "11" in counts[3] else 0
    success_prob = (
        (count_00 + count_01 + count_10 + count_11)/(shots * 4) #qiskit maps 01=>10
    )
    return success_prob

def measure_circuit():
    qc = QuantumCircuit(2)
    qc.measure_all()
    return qc

def prepare_bit_circuit(bit_array):
    """create a circuit that writes a binary qubit string into the register.

    Args:
        bit_array ([int]): binary state to prepare

    Returns:
        QuantumCircuit: circuit with the given binary state
    """
    n = len(bit_array)
    qc = QuantumCircuit(n)
    
    for i in range(0,n):
        if bit_array[i] == 1:
            qc.x(i)
    return qc
