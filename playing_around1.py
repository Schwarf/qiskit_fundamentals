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

initial_state3 = [1/sqrt(2), 1j/sqrt(2)]  # Define state |q_0>
initial_state4 = [sqrt(3)/sqrt(4), 1j/sqrt(4)]  # Define state |q_0>
initial_state5 = [sqrt(3)/sqrt(7), sqrt(4)/sqrt(7)]  # Define state |q_0>

qc3 = QuantumCircuit(1) # Must redefine qc
qc3.initialize(initial_state3, 0) # Initialize the 0th qubit in the state `initial_state`
qc3.save_statevector() # Save statevector
qobj = assemble(qc3)
state = sim.run(qobj).result().get_statevector() # Execute the circuit
print(state)           # Print the result

qobj = assemble(qc3)
results = sim.run(qobj).result().get_counts()
plot_histogram(results)


qc4 = QuantumCircuit(1) # Must redefine qc
qc4.initialize(initial_state4, 0) # Initialize the 0th qubit in the state `initial_state`
qc4.save_statevector() # Save statevector
qobj = assemble(qc4)
state = sim.run(qobj).result().get_statevector() # Execute the circuit
print(state)           # Print the result

qobj = assemble(qc4)
results = sim.run(qobj).result().get_counts()
plot_histogram(results)


qc5 = QuantumCircuit(1) # Must redefine qc
qc5.initialize(initial_state5, 0) # Initialize the 0th qubit in the state `initial_state`
qc5.save_statevector() # Save statevector
qobj = assemble(qc5)
state = sim.run(qobj).result().get_statevector() # Execute the circuit
print(state)           # Print the result

qobj = assemble(qc5)
results = sim.run(qobj).result().get_counts()
plot_histogram(results)

plt.show()
