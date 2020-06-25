# Device Independent Tests for Quantum Networks

*A prototype test suite for verifying unknown quantum devices.*

The quantum internet will enable long-distance quantum cryptography, teleportation, and distributed quantum computation. Inevitably, long-distance quantum communications will require a large network of intermediary quantum-enabled devices. In a quantum network, a handshake protocol is required to verify the quantum capabilities of unknown quantum devices. 

Our goal is to deliver a device independent test suite which verifies a handful of quantum properties of unknown devices. The protocols we provide will test bipartite communication scenarios where one device is trusted and the other is to be verified. The objective is to use measurement statistics to learn whether an unknown device is capable of superpostion, measurement incompatibility, or entanglement sharing.

During this hackathon, we plan to prototype tests that help verify the following quantum properties.

1. **Dimensionality** - Witnesses the minimal dimension of a hilbert space.
2. **Superpostion** - Verifies the ability to prepare and measure quantum superpositions.
3. **Measurement Incompatibility** - Verifies incompatible measurements through a bell violation on a qubit state.
4. **Entanglement** - Witenesses entanglement by violating the Clauser Horne Shimony Holt inequality.

In the future, a trusted quantum node may apply these tests by asking an unknown device to cooperate in order to jointly violate or achieve some classical or quantum bound. The measurement statistics of the tests are sufficient to determine if the unknwown device performed its protocol correctly. A test failure indicates a few possibilities,

1. The unknown device is misaligned with the trusted device and further alignment is required for success.
2. The unknown device is not capable of performing the protocol because it lacks a quantum property.

These tests are not perfect because there is always some uncertainty around the trust of a device. A malicious hacker could attack these tests by creating a hidden communication channel or hidden correlation between the trusted and untrusted device. However, the effectiveness of our tests will improve with scale because community verification will enable a consensus to be formed.

We note that our device independent tests are only a proof of concept on the IBM quantum computer. The reason is that both of our tested parties are being run on the IBM backend. There is no way to verify the trust of either party. Instead, we must trust that the IBM quantum computer works as advertised and that our protocols implemented on the quanum computer can be deployed as a distributed protocol running between nodes of a quantum network.

## Initialize Project

With Makefile: `make init`

or with pip: `pip install -r requirements.txt`

## Run Tests

With Makefile: `make test`

or with python: `python3 -m unittest tests/*.py`



