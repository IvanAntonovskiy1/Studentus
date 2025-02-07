from dis import Positions

from pydantic import BaseModel
import random
from typing import Optional

class Parameters(BaseModel):
    FullName          : str
    NameParameter     : str
    Position          : int
    Value             : float
    UnitsOfMeasure    : str


    def combineNames(self):

        def inner_combine(name: str, value: float, unitsOfMeas: str) -> str:
            return f"{name} = {value}[{unitsOfMeas}] ,"

        # Вызов внутренней функции с атрибутами класса
        return inner_combine(self.FullName, self.Value, self.UnitsOfMeasure)

    @classmethod
    def random ( cls, nameParameter : str, position : int):
        match nameParameter :
            case "V" :
                return cls(NameParameter  = nameParameter                  ,
                           Position       = position                       ,
                           FullName       = nameParameter + position       ,
                           Value          = random.randint(1, 20) ,
                           UnitsOfMeasure = "В"                            )
            case "R" :
                return cls(NameParameter = nameParameter                 ,
                           Position      = position                      ,
                           FullName      = nameParameter + position      ,
                           Value         = random.randrange(500, 5001, 500),
                           UnitsOfMeasure = "ОМ"                         )
            case "C" :
                return cls(NameParameter = nameParameter                 ,
                           Position      = position                      ,
                           FullName      = nameParameter + position      ,
                           Value         = (random.randint(1, 20))/1000000,
                           UnitsOfMeasure = "Ф")
            case "I" :
                return cls(NameParameter = nameParameter                 ,
                           Position      = position                      ,
                           FullName      = nameParameter + position      ,
                           Value         = random.randint(1, 20)/100000,
                           UnitsOfMeasure = "Гн"                         )
            case "TP":
                return cls(NameParameter=nameParameter                   ,
                           Position=position                             ,
                           FullName=nameParameter                        ,
                           Value=random.randint(10, 20)        ,
                           UnitsOfMeasure = "c"                         )


