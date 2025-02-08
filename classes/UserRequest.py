from pydantic import BaseModel
from typing import Optional

#JSON
#'{"id": "kashdkasjhd", "level": 1, "type": 0}'
class UserRequest(BaseModel):
    id            : str            # айди запроса которая будет храниться как лист у юзера и как название к задаче
    formatShem    : int            # уровень задачи которая нужна (ПОМЕНЯТЬ НА NAME_SHEM)
    type          : int            # тип схемы или рандом
