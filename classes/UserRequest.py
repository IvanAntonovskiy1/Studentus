from pydantic import BaseModel
from typing import Optional

#JSON
#'{"id": "kashdkasjhd", "level": 1, "type": 0}'
class UserRequest(BaseModel):
    id            : str            # айди запроса которая будет храниться как лист у юзера и как название к задаче
    level         : int            # уровень задачи которая нужна
    type          : int            # тип схемы или рандом
