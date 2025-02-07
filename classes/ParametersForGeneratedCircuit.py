from pydantic import BaseModel
from typing import Optional

from classes.Parameters import Parameters


class ParametersForGeneratedCircuit(BaseModel):
    circuitName   : Optional[int]
    voltageSource : list[Parameters]                      # возможно одно, а может быть и лист
    timePulse     : Parameters
    Resistor      : list[Parameters]                      # надо сделать лист значений
    Capacitor     : Optional[list[Parameters]]             # надо сделать лист значений
    Inductor      : Optional[list[Parameters]]             # надо сделать лист значений

class RandomParameterForCircuit(BaseModel):
        Voltage   : list[Parameters]
        Capacitor : list[Parameters]
        Resistor  : list[Parameters]
        Inductor  : list[Parameters]
        TimePulse : Parameters

