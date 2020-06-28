import numpy as np
from qiskit import QuantumCircuit

# @brief    Runs the incompatible measurements test
# @detail   Creates and runs all cases x={0,1,2,3} and y={0,1}
#               then determines if the bell inequality has been violated
# @params   dispatcher: quantum dispatcher to run operations
#           tolerance: tolerance on how close to classical results
#               the violation can get
#           shots: number of shots to run
# @returns  Pass/Fail and the bell violation value
def run_test(dispatcher, tolerance, shots):

    pre_ops = [bb84_states()]
    post_ops = [[QuantumCircuit(4)],
                [measure_circuit(0),measure_circuit(1)]]

    # send to dispatcher to run
    counts = dispatcher.batch_run_and_transmit([0,1,2,3],[0,1,2,3],
                pre_ops,post_ops,shots)

    # parse and calculate bell violation
    violation = bell_violation(counts[0],counts[1],shots,shots)

    return (violation - tolerance > 0,violation)

# @brief   Create's Alice's half of the incompatibility
#           measurement circuit.
# @detail  Returns a 4 qubit circuit where the states on
#           the registers are 0, 1, +, and -
# @returns 4 qubit QuantumCircuit
def bb84_states():
    qc = QuantumCircuit(4)
    qc.x(1) # create 1
    qc.h(2) # create +
    qc.x(3) # create -
    qc.h(3) # ^
    return qc

# @brief   Create's Bob's half of the incompatibility
#           measurement circuit.
# @detail  Returns a 4 qubit circuit which applies a y rotation
#           to each register
# @params  y: 0 or 1. Bob's parameter. -pi/4 or -3pi/4 rotation
# @returns 4 qubit QuantumCircuit
def measure_circuit(y):
    assert y == 0 or y == 1, "Bob's input should be 0 or 1"
    qc = QuantumCircuit(4)
    theta = -1.0*(np.pi/4 + 0.5*y*np.pi)
    qc.u3(theta,0,0,range(0,4))
    qc.measure_all()
    return qc

# Computes the amount of violation of the measurement incompatibility bell inequality
#
#	6 >= p(0|00) + p(1|10) + p(0|20) + p(1|30) + p(1|01) + p(0|11) + p(0|21) + p(1|31)
#
# The quantum strategy we are applying achieves 6.828 agianst this inequality.
#
# Inputs:
#	y0/y1_counts: count dictionaries qiskit, jobs().result().get_counts(circ).
#	y0/y1_shots: number of shots used for each respective test
#
# Output:
#	violation: Float, if positive, probabilities violate, if negative, no violation is present
def bell_violation(y0_counts, y1_counts, y0_shots, y1_shots):
	classical_bound = 6

	y0_probs = conditional_probs(y0_counts, y0_shots)
	y1_probs = conditional_probs(y1_counts, y1_shots)

	violation = bell_score(y0_probs, y1_probs) - classical_bound

	return violation

# Computes the score against the measurement incompatibility bell inequality
#
# Inputs:
#	y0/1_probs: np.array() contains conditional outcome probabilities for the test
#
# Output:
#	bell_score: float, the value computed against the bell inequality
def bell_score(y0_probs, y1_probs):
	y0_facet_mask = np.array([[1,0,1,0],[0,1,0,1]])
	y1_facet_mask = np.array([[0,1,1,0],[1,0,0,1]])

	bell_score = np.sum(y0_facet_mask * y0_probs + y1_facet_mask * y1_probs)

	return bell_score

# Inputs:
#	counts: Dictionary, value from qiskit, jobs().result().get_counts(circ).
#	shots: Integer, number of shots used while executing the job
#
# Output:
#	conditionals: 2x4 matrix of conditional probabilities index [b,x] corresponds to p(b|x),
#	              note that y values are constant for a job.
def conditional_probs(counts, shots):

	# Conditional probailites p(b|xy), y is constant for a run on the quantum computer.
	# The conditionals can be written in a 2x4 matrix as p(b|x).
	aggregate_counts = np.zeros((2,4))

	# iterate over keys of counts dictionary
	for outcome in counts:
		# end of count keys is the first qubit so column ids decrement
	    for i in range(0,4):
	        row_id = int(outcome[i])
	        col_id = 3 - i

	        aggregate_counts[row_id,col_id] += counts[outcome]

	# convert bins to probibilities
	conditionals = aggregate_counts / shots

	return conditionals
