import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_bloch_multivector
from math import pi

sim = Aer.get_backend('aer_simulator')

#  U(θ,ϕ,λ)=[[       cos(θ/2), −exp(iλ)sin(θ/2)   ],
#            [exp(iϕ)sin(θ/2), exp(i(ϕ+λ))cos(θ/2)]]

qubit = 0
theta = pi/2
phi = 0
lamb = pi
qc1 = QuantumCircuit(1)
qc1.u(theta, phi, lamb, qubit)
qc1.draw()
qc1.save_statevector()
qobj_h = assemble(qc1)
state = sim.run(qobj_h).result().get_statevector()
plot_bloch_multivector(state, title="Hadamard constructed from u-gate applied")



qc2 = QuantumCircuit(1)
qc2.h(qubit)
qc2.draw()
qc2.save_statevector()
qobj_h = assemble(qc2)
state = sim.run(qobj_h).result().get_statevector()
plot_bloch_multivector(state, title="Hadamard gate applied")
plt.show()
