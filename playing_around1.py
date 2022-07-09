import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi

qc1 = QuantumCircuit(1)  # Create a quantum circuit with one qubit
initial_state = [0,1]   # Define initial_state as |1>
qc1.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
qc1.draw(output='mpl', filename="one_qubit_circuit.png")  # Let's view our circuit
#qc1.draw()

sim = Aer.get_backend('aer_simulator')  # Tell Qiskit how to simulate our circuit
qc2 = QuantumCircuit(1)  # Create a quantum circuit with one qubit
initial_state = [0,1]   # Define initial_state as |1>
qc2.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
qc2.save_statevector()   # Tell simulator to save statevector
qobj = assemble(qc2)     # Create a Qobj from the circuit for the simulator to run
result = sim.run(qobj).result() # Do the simulation and return the result
out_state = result.get_statevector()
print(out_state) # Display the output state vector

qc2.measure_all()
qc2.draw(output='mpl', filename="measure_all.png")
#qc2.draw()

qobj = assemble(qc2)
result = sim.run(qobj).result()
counts = result.get_counts()
plot_histogram(counts)
plt.show()

initial_state = [1/sqrt(2), 1j/sqrt(2)]  # Define state |q_0>