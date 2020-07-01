# Device Independent Tests for Quantum Networks

[![stable](https://img.shields.io/badge/docs-stable-blue.svg)](https://chitambarlab.github.io/QiskitSummerJam2020/index.html)

### *A test suite for verifying unknown quantum devices.*

Project Website: [chitambarlab.github.io/QiskitSummerJam2020/index.html](https://chitambarlab.github.io/QiskitSummerJam2020/index.html)

## Motivation

The quantum internet will enable long-distance quantum cryptography, teleportation, and distributed quantum computation. Inevitably, long-distance quantum communications will require a large network of intermediary quantum-enabled devices [1]. As the size the size of quantum networks increases, a handshake protocol will be required to establish connections with unknown devices. It will be an important part of this handshake to determine whether a device can faithfully perform simple quantum communications tasks. 

## Objectives

1. ***Develop a device-independent handshake protocol to verify quantum systems***
    * Verifies dimension, superposition, incompatible measurements, and entanglement.
    * Applies genericly to future quantum networks of any design.
    * Protocol is documented on the [Verification Protocol page](https://chitambarlab.github.io/QiskitSummerJam2020/device_independent_handshake_protocol.html).
2. ***Create a python module to perform the handshake protocol***
    * The `device_independent_test` module provides a `HandShake` api for running varios device-independent tests for bipartite communication scenarios.
    * Our code is found at: [https://github.com/ChitambarLab/QiskitSummerJam2020](https://github.com/ChitambarLab/QiskitSummerJam2020)
    * Software documentation is located under the 'Software Documentation' tab on the left-hand side
3. ***Prototype and test the handshake with Qiskit***
    * Descriptions of test implementations on the Qiskit simulator and IBM quantum computers is found under the Qiskit Examples tab.
    * The theory behind device independent tests is documented under the 'Device-Independence Theory' tab on the left-hand size.
    
    
## About the Team

We are an interdisciplinary group of PhD students working under Eric Chitambar in the Coordinated Science Lab at University of Illinois Urbana-Champaign.

### Members

* Chloe Kim
* Xinan Chen
* Louis Schatzki
* Brian Doolittle

## Usage Guide

The best way to consume our project is through this website. All notebooks have been converted into a static website made with `mkdocs` and hosted with GitHub pages. 

Our codebase is found on github, [https://github.com/ChitambarLab/QiskitSummerJam2020](https://github.com/ChitambarLab/QiskitSummerJam2020).

The `device_independent_test` module contains python software for running our `HandShake.test_all()` test suite in a generic manner. The `quantum_communicator` module serves as the interface between our `HandShake` module and the quantum devices. For the scope of this project we ran all tests for quantum devices on a single quantum machine.

Please review the [Software Documentation](https://chitambarlab.github.io/QiskitSummerJam2020/Device_Independent_Test_Documentation.html) and [Qiskit Examples](https://chitambarlab.github.io/QiskitSummerJam2020/Classical_Dimension_Test.html) for details regarding project use. 

## Initialize Project

With Makefile: `make init`

or with pip: `pip install -r requirements.txt`

## Run Tests

With Makefile: `make test`

or with python: `python3 -m unittest tests/*.py`

## Build Docs

The documentation is built using `nbconvert` and `mkdocs` to make a static site generated from the jupyter notebooks in this project.

Load a conda environment for site building: `make build.env`

Convert Jupyter notebooks to markdown: `make build.site`

Host project docs locally: `mkdocs serve`

Cleanup the docs folder before builds with: `make clean.site`

## References

[1] Wehner, Stephanie, David Elkouss, and Ronald Hanson. "Quantum internet: A vision for the road ahead." *Science* 362.6412 (2018).

Deploy the docs to github-pages (only run from master): `mkdocs gh-deploy` 






