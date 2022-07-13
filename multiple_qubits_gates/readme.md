# Qubit ordering in Qiskit
Within the physics community, the qubits of a multi-qubit systems are typically ordered with the first qubit on the
left-most side of the tensor product and the last qubit on the right-most side. For instance, if the first qubit is
in state |0> and second is in state |1>, their joint state would be |01>. Qiskit uses a slightly different ordering of
the qubits, in which the qubits are represented from the most significant bit (MSB) on the left to the least
significant bit (LSB) on the right (little-endian). This is similar to bitstring representation on classical
computers, and enables easy conversion from bitstrings to integers after measurements are performed.
For the example just given, the joint state would be represented as |10>.
Importantly, this change in the representation of multi-qubit states affects the way multi-qubit gates are
represented in Qiskit, as discussed below. The representation used in Qiskit enumerates the basis vectors in
increasing order of the integers they represent. For instance, the basis vectors for a 2-qubit system would be
ordered as |00>, |01>, |10>, and |11>. Thinking of the basis vectors as bit strings,
they encode the integers 0,1,2 and 3, respectively.

# Two bit gates
- controlled Pauli gates
- controlled Hadamard gate
- controleld rotation gates
- controlled pahes gate
- controlled u3 gate
- swap gate

# Three bit gates
- Toffoli gate
- Fredkin gate