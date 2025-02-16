from classes.JsonAnswer import JsonAnswer


def checkAnswer(request : JsonAnswer):
    request.validate_Answer()
    return request