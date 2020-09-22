
### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
import numpy as np
from math import sqrt, pi
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def build_state():
    
    # create a quantum circuit on one qubit
    circuit = QuantumCircuit(1)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    
    # apply necessary gates
    initial_state = [1/sqrt(2), -1j/sqrt(2)]
    circuit.initialize(initial_state, 0)
    circuit.rx(pi/2, 0)
    
    # alternate answer 
    # circuit.x(0)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    return circuit
