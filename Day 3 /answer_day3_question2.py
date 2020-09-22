
### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def build_state():
    
    # create a quantum circuit on two qubits
    circuit = QuantumCircuit(2)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    
    # apply necessary gates
    circuit.h(0)
    circuit.x(1)
    circuit.cx(0,1)
    circuit.z(1)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    return circuit
