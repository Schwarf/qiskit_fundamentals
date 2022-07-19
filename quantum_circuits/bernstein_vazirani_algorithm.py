import numpy as np
from matplotlib import pyplot as plt
from qiskit import Aer
from qiskit import QuantumCircuit, assemble, transpile
from qiskit.circuit import Gate
from qiskit.visualization import plot_histogram


def bernstein_vazirani_circuit(oracle_gate: Gate, number_of_inputs: int) -> QuantumCircuit:
    number_of_bits = number_of_inputs
    number_of_qubits = number_of_inputs + 1
    bv_circuit = QuantumCircuit(number_of_qubits, number_of_bits)
    # all qubits initialize to |0> ... last one shall be initialized to |-> ...0-indexed
    bv_circuit.z(number_of_inputs)
    # Apply Hadamard to all input-qubits and the last one
    for qubit in range(number_of_qubits):
        bv_circuit.h(qubit)
    # Apply oracle function: Note this function is applied to all qubits, although is has only an effect on the last
    # qubit
    bv_circuit.append(oracle_gate, range(number_of_qubits))
    # Apply Hadamard to input qubits, the last qubit can now be ignored (in the next step measurement only applied to
    # input)
    for qubit in range(number_of_inputs):
        bv_circuit.h(qubit)

    for classic_bit in range(number_of_bits):
        bv_circuit.measure(classic_bit, classic_bit)

    return bv_circuit
