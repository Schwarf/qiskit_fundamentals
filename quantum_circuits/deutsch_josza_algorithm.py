# initialization
import numpy as np
from matplotlib import pyplot as plt

# importing Qiskit
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, assemble, transpile

# import basic plot tools
from qiskit.visualization import plot_histogram


input_size = 3
const_oracle = QuantumCircuit(input_size + 1)

output = np.random.randint(2)
if output == 1:
    const_oracle.x(input_size)
const_oracle.draw()

balanced_oracle = QuantumCircuit(input_size+1)
b_str = "101"

# Place X-gates
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        balanced_oracle.x(qubit)

# Use barrier as divider
balanced_oracle.barrier()

# Controlled-NOT gates
for qubit in range(input_size):
    balanced_oracle.cx(qubit, input_size)

balanced_oracle.barrier()
# Place X-gates
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        balanced_oracle.x(qubit)

# Show oracle
balanced_oracle.draw()

# ALGORITHM STARTS HERE

dj_circuit = QuantumCircuit(input_size+1, input_size)

# Apply H-gates
for qubit in range(input_size):
    dj_circuit.h(qubit)

# Put qubit in state |->
dj_circuit.x(input_size)
dj_circuit.h(input_size)

# Add oracle
dj_circuit += const_oracle

# Repeat H-gates
for qubit in range(input_size):
    dj_circuit.h(qubit)
dj_circuit.barrier()

# Measure
for i in range(input_size):
    dj_circuit.measure(i, i)

dj_circuit.draw()

aer_sim = Aer.get_backend('aer_simulator')
qobj = assemble(dj_circuit, aer_sim)
results = aer_sim.run(qobj).result()
answer = results.get_counts()

plot_histogram(answer)

plt.show()

