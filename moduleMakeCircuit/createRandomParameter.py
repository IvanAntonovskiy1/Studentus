from classes.Parameters import Parameters
from classes.ParametersForGeneratedCircuit import RandomParameterForCircuit, ParametersForGeneratedCircuit



def getLevelParameter(formatShem : int):
    match formatShem:
        case 1:
            return RandomParameterForCircuit(Voltage   = [Parameters.random("V", "1")],
                                             Resistor  = [Parameters.random("R", "1")],
                                             Capacitor = [Parameters.random("C", "1")],
                                             Inductor  = [Parameters.random("L", "1")],
                                             TimePulse =  Parameters.random("TP","1") )
        case 2:
            return RandomParameterForCircuit(Voltage   = [Parameters.random("V", "1")],
                                             Resistor  = [Parameters.random("R", "1")],
                                             Capacitor = [Parameters.random("C", "1")],
                                             Inductor  = [Parameters.random("L", "1")],
                                             TimePulse =  Parameters.random("TP","1") )
        case 3:
            return RandomParameterForCircuit(Voltage  = [Parameters.random("V", "1")],
                                            Resistor  = [Parameters.random("R", "1"),
                                                         Parameters.random("R", "2")],

                                            Capacitor = [Parameters.random("C", "1")],
                                            Inductor  = [Parameters.random("L", "1")],
                                            TimePulse =  Parameters.random("TP","1") )
        case 4:
            return RandomParameterForCircuit(Voltage  = [Parameters.random("V", "1")],
                                            Resistor  = [Parameters.random("R", "1"),
                                                         Parameters.random("R", "2")],

                                            Capacitor = [Parameters.random("C", "1")],
                                            Inductor  = [Parameters.random("L", "1")],
                                            TimePulse =  Parameters.random("TP","1") )
        case _:
            raise ValueError("Не правильный котик")

def myParametersForGeneratedCircuit(typeShem,formatShem, myRandomParameter : RandomParameterForCircuit):
    return ParametersForGeneratedCircuit( circuitType   =  typeShem                    ,
                                          circuitFormat = formatShem                   ,
                                          voltageSource =  myRandomParameter.Voltage   ,
                                          timePulse     =  myRandomParameter.TimePulse ,
                                          Resistor      =  myRandomParameter.Resistor  ,
                                          Capacitor     =  myRandomParameter.Capacitor ,
                                          Inductor      =  myRandomParameter.Inductor
                                          )