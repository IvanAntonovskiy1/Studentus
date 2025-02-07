from classes.ParametersForGeneratedCircuit import RandomParameterForCircuit


def questionForTheTask(t, t_imp, parameter):
    return f"""Вам схема состоящая из источника импульсного напряжения , резистора(ов) и конденсатора(ов) или катушки(ек). Вам нужно най напряжение на нелинейном элементе во время t = {t} если t_импульса = {t_imp}. """ + indicateTheParametersGivenToMe(parameter)[:-1]+"."

def indicateTheParametersGivenToMe(prametrsGeneratedCircuit:RandomParameterForCircuit):
    str = "Вам даны параметры : "
    strForVoltage = "".join(param.combineNames() for param  in prametrsGeneratedCircuit.Voltage )
    strForResistor = "".join(param.combineNames() for param in prametrsGeneratedCircuit.Resistor)
    strForCapacitor = "".join(param.combineNames() for param in prametrsGeneratedCircuit.Capacitor)
    strForInductor = "".join(param.combineNames() for param in prametrsGeneratedCircuit.Inductor)
    return str +strForVoltage+ strForResistor + strForCapacitor # + strForInductor
