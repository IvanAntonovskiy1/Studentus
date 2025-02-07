from PySpice.Spice.Netlist import Circuit
from generateShemTempFile import generateTempFile
from classes.ParametersForGeneratedCircuit import ParametersForGeneratedCircuit


def makeCircuit(paramForGeneratedCircuit : ParametersForGeneratedCircuit):
    circuit = Circuit("name")
    circuit.include(generateTempFile(paramForGeneratedCircuit))
    return circuit

def simulate_circuit (paramForGeneratedCircuit : ParametersForGeneratedCircuit):
    my_circuit = makeCircuit(paramForGeneratedCircuit)
    simulator = my_circuit.simulator(temperature=25, nominal_temperature=25)
    analysis  = simulator.transient(step_time=1e-6, end_time=30e-3)

    return analysis

def visual_result (paramForGeneratedCircuit : ParametersForGeneratedCircuit):
    import matplotlib.pyplot as plt
    plt.plot(simulate_circuit(paramForGeneratedCircuit)['in'])
    plt.plot(simulate_circuit(paramForGeneratedCircuit)['out'])
    plt.legend(['Vin (Pulse)', 'Vout'])
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.title('Response of the Circuit with Ideal Pulse Voltage Source')
    plt.grid()
    plt.show()


