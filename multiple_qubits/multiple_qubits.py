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


# Print unitary trafo as result of kronecker-product oh H x X
# Circuit with two qubits
qc =QuantumCircuit(2)
# apply hadamard gate to first qubit
qc.h(0)
# apply x gate to second qubit
qc.x(1)
qc.draw()
svsim = Aer.get_backend('aer_simulator')
qc.save_unitary()
qobj = assemble(qc)
unitary = svsim.run(qobj).result().get_unitary()
print(unitary)


# Print unitary trafo as result of XZH
qc = QuantumCircuit(1)
qc.h(0)
qc.z(0)
qc.x(0)
qc.draw()
svsim = Aer.get_backend('aer_simulator')
qc.save_unitary()
qobj = assemble(qc)
unitary = svsim.run(qobj).result().get_unitary()
print(unitary)


# Print unitary trafo as result of kronecker-product X x Z x H
qc = QuantumCircuit(3)
qc.h(0)
qc.z(1)
qc.x(2)
qc.draw()
svsim = Aer.get_backend('aer_simulator')
qc.save_unitary()
qobj = assemble(qc)
unitary = svsim.run(qobj).result().get_unitary()
print(unitary)


plt.show()