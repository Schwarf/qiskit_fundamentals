import matplotlib.pyplot as plt
from math import pi
from qiskit import QuantumCircuit, QuantumRegister, assemble, Aer, transpile
import numpy as np

backend = Aer.get_backend('unitary_simulator')
def controlled_u_gate_two_qubit_gates(qubits: QuantumRegister, circuit: QuantumCircuit, theta: float) -> QuantumCircuit:
    target = qubits[2]
    control1 = qubits[0]
    control2 = qubits[1]
    circuit.cp(theta, control2, target)
    circuit.cx(control1, control2)
    circuit.cp(-theta, control2, target)
    circuit.cx(control1, control2)
    circuit.cp(theta, control1, target)
    circuit.draw()
    return circuit

qubits = QuantumRegister(3)

qc = QuantumCircuit(qubits)
qc.ccx(qubits[0], qubits[1], qubits[2])
qc.draw()
    
qubits2 = QuantumRegister(3)
qc2 = QuantumCircuit(qubits2)
controlled_u_gate_two_qubit_gates(qubits2, qc2, np.pi)



job = backend.run(transpile(qc, backend))
result=job.result().get_unitary(qc)
print(result)


job2 = backend.run(transpile(qc2, backend))
result2=job2.result().get_unitary(qc2)
print(result2)

plt.show()


