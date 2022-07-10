from matplotlib import pyplot as plt
from qiskit import QuantumCircuit, Aer, assemble
import numpy as np
from qiskit.visualization import plot_histogram, plot_bloch_multivector

# Three qubits
qc = QuantumCircuit(3)
# Apply H-gate to each qubit:
for qubit in range(3):
    qc.h(qubit)
# See the circuit:
qc.draw()

# Visualize result
svsim = Aer.get_backend('aer_simulator')
qc.save_statevector()
qobj = assemble(qc)
final_state = svsim.run(qobj).result().get_statevector()
print(final_state)


# Circuit with two qubits
qc =QuantumCircuit(2)
# apply hadamard gate to first qubit
qc.h(0)
# apply x gate to second qubit
qc.x(1)
qc.draw()
svsim = Aer.get_backend('aer_simulator')
qc.save_statevector()
qobj = assemble(qc)
final_state = svsim.run(qobj).result().get_statevector()
print(final_state)

plt.show()