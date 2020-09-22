
### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def build_state():
    
    # create a quantum circuit on one qubit
    circuit = QuantumCircuit(1)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    
    # apply necessary gates
    circuit.initialize([0,1],0)
    circuit.ry(np.pi/3,0)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    return circuit