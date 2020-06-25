import numpy as np

# Computes the amount of violation of the measurement incompatibility bell inequality
#
#	6 >= p(0|00) + p(1|10) + p(0|20) + p(1|30) + p(1|01) + p(0|11) + p(0|21) + p(1|31)
#
# The quantum strategy we are applying achieves 6.818 agianst this inequality.
#
# Inputs:
#	y0/y1_counts: count dictionaries qiskit, jobs().result().get_counts(circ).
#	y0/y1_shots: number of shots used for each respective test
#
# Output:
#	violation: Float, if positive, probabilities violate, if negative, no violation is present 
def bell_violation(y0_counts, y1_counts, y0_shots, y1_shots):
	classical_bound = 6

	probs_y0 = conditional_probs(y0_counts, y0_shots)
	probs_y1 = conditional_probs(y1_counts, y1_shots)

	bell_score_y0 = probs_y0[0,0] + probs_y0[1,1] + probs_y0[0,2] + probs_y0[1,3]
	bell_score_y1 = probs_y1[1,0] + probs_y1[0,1] + probs_y1[0,2] + probs_y1[1,3]

	violation = bell_score_y0 + bell_score_y1 - classical_bound

	return violation


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
