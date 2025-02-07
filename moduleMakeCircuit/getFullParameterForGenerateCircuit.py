from classes.UserRequest import UserRequest


# Функция getParameterForSimulate преобразует входящий JSON в класс UserRequest для дальнейшей работы

def getParameterForSimulate(JSON):
    return UserRequest.model_dump(JSON)

