import numpy as np

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
