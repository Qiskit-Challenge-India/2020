
### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def build_state():
    
    # initialize a 3 qubit circuit
    circuit = QuantumCircuit(3)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    
    # apply necessary gates
    circuit.h(0)
    circuit.cx(0,1)
    circuit.cx(1,2)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    return circuit
