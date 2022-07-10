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

qc_x = QuantumCircuit(1)
qc_x.x(0)
qc_x.draw(output='mpl', filename="x_gate_applied_to_0.png")

qc_x.save_statevector()
qobj_x = assemble(qc_x)
state = sim.run(qobj_x).result().get_statevector()
plot_bloch_multivector(state, title="X gate applied")
plt.show()
