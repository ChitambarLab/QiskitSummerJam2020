
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
    assert y == 0 or 1
    qc = QuantumCircuit(4)
    theta = -1.0*(np.pi/4 + 0.5*y*np.pi)
    qc.u3(theta,0,0,range(0,4))
    qc.measure_all()
    return qc

# @brief    Runs multiple jobs
# @params   qc: an arry of circuits to run
#           bckend: the backend to run the circuits on
# @returns  A managed_job object containing jobs for all circuits
# @note     cannot control the number of shots, is always 1000
def run_jobs(qc,bckend):
    job_manager = IBMQJobManager()
    job_set = job_manager.run(qc, backend=bckend, name='msrincom_test')
    job_set.error_messages()
    return job_set
