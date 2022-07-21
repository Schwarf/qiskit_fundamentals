from matplotlib import pyplot as plt
# importing Qiskit
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram
from qiskit_textbook.tools import simon_oracle


def simon_circuit(binary_string: str) -> QuantumCircuit:
    n = len(binary_string)
    s_circuit = QuantumCircuit(2*n, n)
    s_circuit.h(range(n))
    s_circuit.barrier()
    s_circuit += simon_oracle(binary_string)
    s_circuit.barrier()
    s_circuit.h(range(n))
    # TODO: Shouldn't it be the second register to be measured?
    s_circuit.measure(range(n), range(n))
    return s_circuit

binary_string = "110"

simon_circuit = simon_circuit(binary_string)
simon_circuit.draw()

aer_sim = Aer.get_backend('aer_simulator')
shots = 1024
qobj = assemble(simon_circuit, shots=shots)
results = aer_sim.run(qobj).result()
counts = results.get_counts()
plot_histogram(counts)

plt.show()
