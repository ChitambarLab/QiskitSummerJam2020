from qiskit import QuantumCircuit

# create two-qubit entangled circuit
def create_entangled_circuit():
  qc = QuantumCircuit(2)
  qc.h(0)
  qc.cx(0,1)
  return qc

# measure a given circuit in the ZW basis
def measure_in_ZW(qc):
  qc.s(1)
  qc.h(1)
  qc.t(1)
  qc.h(1)
  return qc.measure_all()

# measure a given circuit in the ZV basis
def measure_in_ZV(qc):
  qc.s(1)
  qc.h(1)
  qc.tdg(1)
  qc.h(1)
  return qc.measure_all()

# measure a given circuit in the XW basis
def measure_in_XW(qc):
  qc.h(0)
  qc.s(1)
  qc.h(1)
  qc.t(1)
  qc.h(1)
  return qc.measure_all()

# measure a given circuit in the XV basis
def measure_in_XV(qc):
  qc.h(0)
  qc.s(1)
  qc.h(1)
  qc.tdg(1)
  qc.h(1)
  return qc.measure_all()