from pydantic import BaseModel
from typing import Optional

class Answer(BaseModel):                                  # переименовать во что то подходящие
    id            : int
    time          : Optional[float]                       # время
    voltage       : Optional[float]                       # напряжение

    def __hash__(self):
        return hash((self.time,self.voltage))

    def __eq__(self, other):
        if isinstance(other,Answer):
            return  self.time == other.time and self.voltage == other.voltage
        return False