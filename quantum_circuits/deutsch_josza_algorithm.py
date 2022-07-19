import numpy as np
from matplotlib import pyplot as plt
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, assemble, transpile
from qiskit.circuit import Gate
from qiskit.visualization import plot_histogram



def _constant_oracle(oracle_qc: QuantumCircuit, number_of_inputs: int) -> QuantumCircuit:
    # For a constant oracle we just have to choose 0 or 1 and set the out-put qubit accordingly
    output_value = np.random.randint(2)
    # If output_value is one, we set the output-qubit (the last one) to |1>
    if output_value == 1:
        oracle_qc.x(number_of_inputs)
    return oracle_qc

def _balanced_oracle(oracle_qc: QuantumCircuit, number_of_inputs: int) -> QuantumCircuit:
    # For a balanced oracle we use CNOT gates that take on one-inout qubit as control and target the output qubit
    # To randomize we randomly wrap (befor and after CNOT) input-qubits with X-gates.

    # Generate random number between 1 and 2**n-1 (n =number__of_inputs) ... the corresponding binary string
    # tells us the positions of the qubits that will be wrapped in X-gates
    random_binary_string_number = np.random.randint(1, 2 ** number_of_inputs)
    random_binary_string = format(random_binary_string_number, '0' + str(number_of_inputs) + 'b')
    # Now place first X-gates
    for qubit_position in range(len(random_binary_string)):
        if random_binary_string[qubit_position] == 1:
            oracle_qc.x(qubit_position)

    # Now we apply the CNOT gates to all qubits
    for qubit_position in range(number_of_inputs):
        oracle_qc.cx(qubit_position)
    # Now place the final X-gates
    for qubit_position in range(len(random_binary_string)):
        if random_binary_string[qubit_position] == 1:
            oracle_qc.x(qubit_position)

    return oracle_qc

def construct_oracle(number_of_inputs: int, is_constant_oracle: False) -> Gate:
    # There is one output-qubit (the last one) which is either 1 or 0.
    number_of_outputs = 1
    number_of_qubits = number_of_inputs + number_of_outputs

    oracle_qc = QuantumCircuit(number_of_qubits)

    if is_constant_oracle:
        qc_oracle = _constant_oracle(oracle_qc, number_of_inputs)
    if not is_constant_oracle:
        qc_oracle = _balanced_oracle(oracle_qc, number_of_inputs)

    # Create the gate
    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = "Oracle"
    return oracle_gate

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

