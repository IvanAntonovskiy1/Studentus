import tempfile
from classes.ParametersForGeneratedCircuit import ParametersForGeneratedCircuit



def generateTempFile(param : ParametersForGeneratedCircuit):
    circuitDescription = makeCircuitDescription(param)
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.cp', delete=False) as temp_file:
        temp_file.write(circuitDescription)
        temp_file_path = temp_file.name

    return temp_file_path

# def makeCircuitDescription(param : ParametersForGeneratedCircuit):
#     match param.circuitName:
#         case 11 :
#             return f"""
#             {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
#             {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
#             {param.Capacitor[0].FullName} out 0 {param.Capacitor[0].Value}
#             .end
#             """
#         case 12 :
#             return f"""
#             {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
#             {param.Capacitor[0].FullName} in out {param.Capacitor[0].Value}
#             {param.Resistor[0].FullName} out 0 {param.Resistor[0].Value}
#             .end
#             """
#         case 13 :
#             return f"""
#             {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
#             {param.Resistor[0].FullName} in node1 {param.Resistor[0].Value}
#             {param.Capacitor[0].FullName} node1 out {param.Capacitor[0].Value}
#             {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
#             .end
#             """
#         case 14 :
#             return f"""
#             {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
#             {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
#             {param.Capacitor[0].FullName} out 0 {param.Capacitor[0].Value}
#             {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
#             .end
#             """
# # --------------------------------для катушки сделать---------------------------------------------------
#         case 21 :
#             return f"""
#             {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
#             {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
#             {param.Inductor[0].FullName} out 0 {param.Inductor[0].Value}
#             .end
#             """
#         case 22 :
#             return f"""
#             {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
#             {param.Inductor[0].FullName} in out {param.Inductor[0].Value}
#             {param.Resistor[0].FullName} out 0 {param.Resistor[0].Value}
#             .end
#             """
#         case 23 :
#             return f"""
#             {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
#             {param.Resistor[0].FullName} in node1 {param.Resistor[0].Value}
#             {param.Capacitor[0].FullName} node1 out {param.Capacitor[0].Value}
#             {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
#             .end
#             """
#         case 24 :
#             return f"""
#             {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
#             {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
#             {param.Capacitor[0].FullName} out 0 {param.Capacitor[0].Value}
#             {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
#             .end
#             """
#  # -----------------------------------------------------------------------------------
#         case _:
#             raise ValueError("Не правильный код")
#
#
#
#



def makeCircuitDescription(param : ParametersForGeneratedCircuit):
    match param.circuitType:
        case 1 :
            match param.circuitFormat:
                case 1 :
                    return f"""
                    {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
                    {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
                    {param.Capacitor[0].FullName} out 0 {param.Capacitor[0].Value} 
                    .end
                    """
                case 2 :
                    return f"""
                    {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
                    {param.Capacitor[0].FullName} in out {param.Capacitor[0].Value}
                    {param.Resistor[0].FullName} out 0 {param.Resistor[0].Value}
                    .end
                    """
                case 3 :
                    return f"""
                    {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
                    {param.Resistor[0].FullName} in node1 {param.Resistor[0].Value}
                    {param.Capacitor[0].FullName} node1 out {param.Capacitor[0].Value} 
                    {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
                    .end
                    """
                case 4 :
                    return f"""
                    {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
                    {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
                    {param.Capacitor[0].FullName} out 0 {param.Capacitor[0].Value} 
                    {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
                    .end
                    """
# --------------------------------для катушки сделать---------------------------------------------------
        case 2 :
            match param.circuitFormat:
                case 1 :
                    print(f"""
                    {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
                    {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
                    {param.Inductor[0].FullName} out 0 {param.Inductor[0].Value} 
                    .end
                    """)
                    return f"""
                    {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
                    {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
                    {param.Inductor[0].FullName} out 0 {param.Inductor[0].Value} 
                    .end
                    """
                case 2 :
                    return f"""
                    {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
                    {param.Inductor[0].FullName} in out {param.Inductor[0].Value}
                    {param.Resistor[0].FullName} out 0 {param.Resistor[0].Value}
                    .end
                    """
                case 3 :
                    return f"""
                    {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
                    {param.Resistor[0].FullName} in node1 {param.Resistor[0].Value}
                    {param.Inductor[0].FullName} node1 out {param.Inductor[0].Value} 
                    {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
                    .end
                    """
                case 4 :
                    return f"""
                    {param.voltageSource[0].FullName} in 0 PULSE(0 {param.voltageSource[0].Value} 0 0 0 {param.timePulse.Value}ms )
                    {param.Resistor[0].FullName} in out {param.Resistor[0].Value}
                    {param.Inductor[0].FullName} out 0 {param.Inductor[0].Value} 
                    {param.Resistor[1].FullName} out 0 {param.Resistor[1].Value}
                    .end
                    """
 # -----------------------------------------------------------------------------------
        case _:
            raise ValueError("Не правильный код")




