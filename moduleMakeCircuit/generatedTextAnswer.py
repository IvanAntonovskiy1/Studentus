from classes.ParametersForGeneratedCircuit import RandomParameterForCircuit


def questionForTheTask(t, t_imp, parameter, type):
    return f"""Вам схема состоящая из источника импульсного напряжения , резистора(ов) и конденсатора(ов) или катушки(ек). Вам нужно най напряжение на нелинейном элементе во время t = {t} если t_импульса = {t_imp}. """ + indicateTheParametersGivenToMe(type,parameter)[:-1]+"."

def indicateTheParametersGivenToMe(type ,prametrsGeneratedCircuit:RandomParameterForCircuit):
    str = "Вам даны параметры : "
    strForVoltage   = "".join(param.combineNames() for param in prametrsGeneratedCircuit.Voltage  )
    strForResistor  = "".join(param.combineNames() for param in prametrsGeneratedCircuit.Resistor )
    strForCapacitor = "".join(param.combineNames() for param in prametrsGeneratedCircuit.Capacitor)
    strForInductor  = "".join(param.combineNames() for param in prametrsGeneratedCircuit.Inductor )
    match type :
        case 1 :
            return str + strForVoltage + strForResistor + strForCapacitor
        case 2 :
            return str + strForVoltage + strForResistor + strForInductor