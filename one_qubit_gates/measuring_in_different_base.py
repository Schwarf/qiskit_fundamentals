from math import sqrt

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram

sim = Aer.get_backend('aer_simulator')


# Create the X-measurement function
# Argumnets are the quantum circuit, the initial qubit and the initial classical bit
def x_measurement(qc, qubit, cbit):
    """Measure 'qubit' in the X-basis, and store the result in 'cbit'"""
    # Go to Z-basis by applying hadamard gate
    qc.h(qubit)
    qc.measure(qubit, cbit)
    return qc


# Create the X-measurement function
# Argumnets are the quantum circuit, the initial qubit and the initial classical bit
def x_measurement_from_z_basis(qc_hzh, qubit, cbit):
    """Measure 'qubit' in the X-basis, and store the result in 'cbit'"""
    # Go to Z-basis by applying hadamard gate
    qc_hzh.h(qubit)
    qc_hzh.z(qubit)
    qc_hzh.h(qubit)
    qc_hzh.measure(qubit, cbit)
    return qc_hzh


# initial state is |-> in X-basis
initial_state = [1 / sqrt(2), -1 / sqrt(2)]
# Create quantum circuit with one qubit and one classical bit
qc = QuantumCircuit(1, 1)
# Initialize with  |-> (X-Basis)
qc.initialize(initial_state, 0)
x_measurement(qc, 0, 0)  # measure qubit 0 to classical bit 0
qc.draw()

qobj = assemble(qc)
counts = sim.run(qobj).result().get_counts()
plot_histogram(counts)

qc_hzh = QuantumCircuit(1, 1)
initial_state_hzh = [1, 0]
qc_hzh.initialize(initial_state_hzh, 0)
x_measurement_from_z_basis(qc_hzh, 0, 0)

qobj_hzh = assemble(qc_hzh)
counts_hzh = sim.run(qobj_hzh).result().get_counts()
plot_histogram(counts_hzh)

plt.show()
