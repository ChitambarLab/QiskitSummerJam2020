from qiskit import QuantumCircuit


def hello():
    print("hello")

# returns x + 2
def add_two(x):
    return x + 2

def parabola(x):
    return x**2

# prepares a 0 qubit and 1 qubit
def prepare_01_circuit():
    circ = QuantumCircuit(2)
    circ.x(1)

    return circ

def measure_circuit(num_qubits):
    num_qubits = 2
    circ = QuantumCircuit(num_qubits)
    circ.measure_all()

    return circ

if __name__ == "__main__":
    hello()