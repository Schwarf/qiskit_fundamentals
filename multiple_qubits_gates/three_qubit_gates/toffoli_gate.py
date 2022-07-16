import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, assemble, Aer, transpile

backend = Aer.get_backend('unitary_simulator')

qubits = QuantumRegister(3)

qc = QuantumCircuit(qubits)
qc.ccx(qubits[0], qubits[1], qubits[2])
qc.draw()

job = backend.run(transpile(qc, backend))
result=job.result().get_unitary(qc, decimals=3)
print(result)
plt.show()
