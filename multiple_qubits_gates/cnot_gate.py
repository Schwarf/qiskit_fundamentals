from matplotlib import pyplot as plt
from qiskit import QuantumCircuit, Aer, assemble
import numpy as np
from qiskit.visualization import plot_histogram, plot_bloch_multivector

qc = QuantumCircuit(2)
# cnot gate. first index is control qubit, second one is target qubit
qc.cx(0, 1)
qc.draw()

plt.show()
