from pydantic import BaseModel
from typing import Optional

from classes.Answer import Answer
from classes.ParametersForGeneratedCircuit import RandomParameterForCircuit


class JsonAnswer(BaseModel):                     # переименовать во что то подходящие
    id               : str                       # id из userRequest
    parameterCircuit : RandomParameterForCircuit
    assignment       : str                       # время
    answer           : Answer                    # напряжение
    formatShem       : int
    type             : int
    linkToPicture    : Optional[str] = None
    myAnswer         : float = 0
    correctAnswer    : bool = False

    def validate_Answer(self):
        if self.myAnswer == self.answer.voltage:
            self.correctAnswer = True