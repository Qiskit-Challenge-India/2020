# the write_and_run function writes the content in this cell into the file "feature_map.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import ZZFeatureMap, ZFeatureMap, PauliFeatureMap
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def feature_map(): 
    # BUILD FEATURE MAP HERE - START
    
    # import required qiskit libraries if additional libraries are required
    
    # build the feature map
    feature_map = PauliFeatureMap(3, reps=1, paulis = ['ZZ', 'Y', 'X'])  # linear = full
    #
    #ZZFeatureMap(feature_dimension = 3, reps = 1, entanglement='full')
    
    # BUILD FEATURE MAP HERE - END
    
    #return the feature map which is either a FeatureMap or QuantumCircuit object
    return feature_map
# the write_and_run function writes the content in this cell into the file "variational_circuit.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.circuit.library import  RealAmplitudes, EfficientSU2
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def variational_circuit():
    # BUILD VARIATIONAL CIRCUIT HERE - START
    
    # import required qiskit libraries if additional libraries are required
    
    # build the variational circuit
    var_circuit = EfficientSU2(3, entanglement='full', reps=5)#, su2_gates = ['rz', 'y', 'x'])
    #RealAmplitudes(num_qubits = 3, entanglement = 'full', reps = 4)
    #

    # BUILD VARIATIONAL CIRCUIT HERE - END
    
    # return the variational circuit which is either a VaritionalForm or QuantumCircuit object
    return var_circuit
# # the write_and_run function writes the content in this cell into the file "optimal_params.py"

### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def return_optimal_params():
    # STORE THE OPTIMAL PARAMETERS AS AN ARRAY IN THE VARIABLE optimal_parameters 
    
    optimal_parameters = [ 1.39627827,  1.71637671,  0.62908663, -0.16653657,  0.00923112,
        2.3733627 ,  0.16140889,  0.28831471,  0.76324818,  0.38969527,
        1.97726566,  1.40016751, -0.08908601, -2.74323277, -0.07396283,
        0.47829233, -1.71283869, -0.2929925 , -0.9554551 ,  4.50369923,
       -0.22263297, -1.91166354,  0.62246693, -1.27931642,  1.27484007,
        1.09475135, -0.07819775, -1.24281102,  1.38282435,  1.24114246,
        1.57188881, -2.46138841,  0.51137798, -0.3384334 , -1.68442421,
       -0.27349316]
    
    # STORE THE OPTIMAL PARAMETERS AS AN ARRAY IN THE VARIABLE optimal_parameters 
    return np.array(optimal_parameters)
