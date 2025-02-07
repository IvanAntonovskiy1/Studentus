import random


#здесь я определяю радомное время для взятия значения ответа
def timeAnswer(TP):
    return random.randint(int(TP) - 8, int(TP)+8)
#здесь я нахожу по выбранному рандомно времени нужный мне ответ
def myAnswer(answerList, answer):
    return next(a for a in answerList if a.time == answer)