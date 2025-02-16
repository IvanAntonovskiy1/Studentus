from classes.JsonAnswer import JsonAnswer
from moduleMakeCircuit.answerRandom import myAnswer, timeAnswer
from moduleMakeCircuit.createRandomParameter import getLevelParameter, myParametersForGeneratedCircuit
from moduleMakeCircuit.generatedTextAnswer import questionForTheTask
from moduleMakeCircuit.gettingDataFromSchema import getAnswerList
from moduleMakeCircuit.makeCircuit import simulate_circuit, visual_result


# написать то чтобы выдавался json файл
def generatedRLCShem(request):
    parametrsGeneratedCircuit = getLevelParameter(request.formatShem)
    myParam = myParametersForGeneratedCircuit(request.type, request.formatShem, getLevelParameter(request.formatShem))
    answer = myAnswer(getAnswerList(simulate_circuit(myParam)),
                      timeAnswer(parametrsGeneratedCircuit.TimePulse.Value))
    jsonAnswer = JsonAnswer(id               = request.id,
                            parameterCircuit = parametrsGeneratedCircuit,
                            assignment       = questionForTheTask(answer.time, parametrsGeneratedCircuit.TimePulse.Value,parametrsGeneratedCircuit, request.type),
                            answer           = answer,
                            formatShem       = request.formatShem,
                            type             = request.type)

    return jsonAnswer

