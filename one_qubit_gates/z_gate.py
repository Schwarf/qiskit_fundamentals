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

qc_z = QuantumCircuit(1)
qc_z.z(0)
qc_z.draw(output='mpl', filename="Z_gate_applied_to_0.png")

qc_z.save_statevector()
qobj_z = assemble(qc_z)
state = sim.run(qobj_z).result().get_statevector()
plot_bloch_multivector(state, title="Z gate applied")
plt.show()
## Note the bloch sphere only shows the relative shares of the two base vectors |0>, |1> phases like -1, i, -i are
## not depicted
