import tempfile
from classes.ParametersForGeneratedCircuit import ParametersForGeneratedCircuit



def generateTempFile(param : ParametersForGeneratedCircuit):
    circuitDescription = makeCircuitDescription(param)
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.cp', delete=False) as temp_file:
        temp_file.write(circuitDescription)
        temp_file_path = temp_file.name

    return temp_file_path

def makeCircuitDescription(param : ParametersForGeneratedCircuit):
    match param.circuitName:
        case 0 :
            return f"""
            {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
            {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
            {param.Capacitor[0].FullName} out 0 {param.Capacitor[0].Value} 
            .end
            """
        case 1 :
            return f"""
            {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
            {param.Capacitor[0].FullName} in out {param.Capacitor[0].Value}
            {param.Resistor[0].FullName} out 0 {param.Resistor[0].Value}
            .end
            """
        case 2 :
            return f"""
            {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
            {param.Resistor[0].FullName} in node1 {param.Resistor[0].Value}
            {param.Capacitor[0].FullName} node1 out {param.Capacitor[0].Value} 
            {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
            .end
            """
        case 3 :
            return f"""
            {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
            {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
            {param.Capacitor[0].FullName} out 0 {param.Capacitor[0].Value} 
            {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
            .end
            """
# --------------------------------для катушки сделать---------------------------------------------------
        case 4 :
            return f"""
            {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
            {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
            {param.Capacitor[0].FullName} out 0 {param.Capacitor[0].Value} 
            .end
            """
        case 5 :
            return f"""
            {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
            {param.Capacitor[0].FullName} in out {param.Capacitor[0].Value}
            {param.Resistor[0].FullName} out 0 {param.Resistor[0].Value}
            .end
            """
        case 6 :
            return f"""
            {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
            {param.Resistor[0].FullName} in node1 {param.Resistor[0].Value}
            {param.Capacitor[0].FullName} node1 out {param.Capacitor[0].Value} 
            {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
            .end
            """
        case 7 :
            return f"""
            {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
            {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
            {param.Capacitor[0].FullName} out 0 {param.Capacitor[0].Value} 
            {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
            .end
            """
 # -----------------------------------------------------------------------------------
        case 888 :
            return f"""
            {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
            {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
            {param.Capacitor[0].FullName} out 0 {param.Capacitor[0].Value} 
            .end
            """
        case _:
            raise ValueError("Не правильный код")




