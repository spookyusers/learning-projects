# Simulate Quantum Circuit

import random
import matplotlib.pyplot as plt
import numpy as np
try:
    import cirq
except ImportError:
    print("Installing cirq...")
    !pip install cirq --quiet
    import cirq
    print("Installed cirq.")

num_qubits = 4
qubits = cirq.NamedQubit.range(num_qubits, prefix = 'q')
q0 = qubits[0]
q1 = qubits[1]
q2 = qubits[2]
q3 = qubits[3]

qc = cirq.Circuit()
qc.append(cirq.H(q0))
qc.append(cirq.CNOT(q0,q1))
qc.append(cirq.H(q2))
qc.append(cirq.CNOT(q2,q3))

print(qc)

sv = cirq.final_state_vector(qc)
ket = cirq.dirac_notation(sv)

print(ket)

qc.append(cirq.M(qubits))

print(qc)

sim = cirq.Simulator()
result = sim.run(qc, repetitions = 100000)

hist = cirq.plot_state_histogram(result, plt.subplot(), title = 'Qubit States', xlabel = 'States', ylabel = 'Occurrences', tick_label=binary_labels(4))

plt.show()
