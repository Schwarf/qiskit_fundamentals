import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_bloch_multivector

sim = Aer.get_backend('aer_simulator')

# Pauli gates
# qubit in state |0>
qc_original = QuantumCircuit(1)

# Apply x-gate
qc_original.save_statevector()
qobj_original = assemble(qc_original)
state = sim.run(qobj_original).result().get_statevector()
plot_bloch_multivector(state, title="original")

qc_y = QuantumCircuit(1)
qc_y.y(0)
qc_y.draw(output='mpl', filename="y_gate_applied_to_0.png")

qc_y.save_statevector()
qobj_y = assemble(qc_y)
state = sim.run(qobj_y).result().get_statevector()
plot_bloch_multivector(state, title="Y gate applied")
plt.show()
## Note the bloch sphere only shows the relative shares of the two base vectors |0>, |1> phases like -1, i, -i are
## not depicted