# initialization
import numpy as np
from matplotlib import pyplot as plt
# importing Qiskit
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, assemble, transpile
from qiskit.circuit import Gate

# import basic plot tools
from qiskit.visualization import plot_histogram


def deutsch_josza_circuit(oracle_gate: Gate, number_of_inputs: int) -> QuantumCircuit:
    number_of_bits = number_of_inputs
    number_of_qubits = number_of_inputs + 1
    dj_circuit = QuantumCircuit(number_of_qubits, number_of_bits)
    # all qubits initialize to |0> ... last one shall be initialized to |1> ...0-indexed
    dj_circuit.x(number_of_inputs)
    # Apply Hadamard to all input-qubits and the last one
    for qubit in range(number_of_qubits):
        dj_circuit.h(qubit)
    # Apply oracle function: Note this function is applied to all qubits, although is has only an effect on the last
    # qubit
    dj_circuit.append(oracle_gate, range(number_of_qubits))
    # Apply Hadamard to input qubits, the last qubit can now be ignored (in the next step measurement only applied to
    # input)
    for qubit in range(number_of_inputs):
        dj_circuit.h(qubit)

    for classic_bit in range(number_of_bits):
        dj_circuit.measure(classic_bit)

    return dj_circuit



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

