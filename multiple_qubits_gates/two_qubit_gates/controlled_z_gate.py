from matplotlib import pyplot as plt
from qiskit import QuantumCircuit, Aer, assemble
from qiskit.visualization import plot_histogram
from typing import List, Tuple

control_qubit = 0
target_qubit = 1
svsim = Aer.get_backend('aer_simulator')


def use_controlled_z(initial_state: Tuple[List[int], int] = None) -> QuantumCircuit:
    qc_direct = QuantumCircuit(2)
    if initial_state:
        qc_direct.initialize(initial_state[0], initial_state[1])
    qc_direct.cz(control_qubit, target_qubit)
    qc_direct.draw()
    qc_direct.save_statevector()
    qobj = assemble(qc_direct)
    result = svsim.run(qobj).result()
    plot_histogram(result.get_counts())


# In specific devices only CNOT (controlled x-gate) can directly applied, that means all other gates have
# to be constructed from CNOT (and e.g. Hadamard)
# Z = HXH

def constructed_controlled_z(initial_state: Tuple[List[int], int] = None) -> QuantumCircuit:
    qc_indirect = QuantumCircuit(2)
    if initial_state:
        qc_indirect.initialize(initial_state[0], initial_state[1])
    qc_indirect.h(target_qubit)
    qc_indirect.cx(control_qubit, target_qubit)
    qc_indirect.h(target_qubit)
    qc_indirect.draw()
    qc_indirect.save_statevector()
    qobj = assemble(qc_indirect)
    result = svsim.run(qobj).result()
    plot_histogram(result.get_counts())


initial_states = [ ([1, 0], target_qubit),
                   ([0, 1], target_qubit),
                   ([1, 0], control_qubit),
                   ([0, 1], control_qubit)]

for initial_state in initial_states:
    use_controlled_z(initial_state)
    constructed_controlled_z(initial_state)

plt.show()
