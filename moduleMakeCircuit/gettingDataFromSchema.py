from classes.Answer import Answer
from collections import OrderedDict
import re


def extract_float_from_string(input_string):
    match = re.search(r"[-+]?\d*\.\d+|\d+", input_string)
    if match:
        return float(match.group())
    else:
        return None


def getAnswerList(analys):
    answerList = []
    for index in range(len(analys.time)):
        time = round(extract_float_from_string(str(analys.time[index])) * 1000)
        voltage_n2 = round(extract_float_from_string(str(analys['out'][index])), +1)
        answer = Answer(id=index,
                        time=time,
                        voltage=voltage_n2
                        )
        if time < 200:
            answerList.append(answer)

    uniqueList = list(OrderedDict.fromkeys(answerList))

    return uniqueList