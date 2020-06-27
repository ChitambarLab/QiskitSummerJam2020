# Entanglement Testing


```python
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.providers.ibmq.managed import IBMQJobManager

# Loading your IBM Q account(s)
import qiskit
from qiskit import IBMQ

import matplotlib.pyplot as plt
import numpy as np

from device_independent_test.entanglement import EntanglementTest

```


```python
test = EntanglementTest()
test.run_CHSH_test(backend="ibmq_qasm_simulator", shots=3000)
```

    ibmqfactory.load_account:WARNING:2020-06-26 16:49:59,854: Credentials are already in use. The existing account in the session will be replaced.





    {'received': 2.844, 'expected': 2.8284271247461903}


