from classes.JsonAnswer import JsonAnswer
from moduleMakeCircuit.answerRandom import myAnswer, timeAnswer
from moduleMakeCircuit.createRandomParameter import getLevelParameter, myParametersForGeneratedCircuit
from moduleMakeCircuit.generatedTextAnswer import questionForTheTask
from moduleMakeCircuit.gettingDataFromSchema import getAnswerList
from moduleMakeCircuit.makeCircuit import simulate_circuit, visual_result


# написать то чтобы выдавался json файл
def generatedRLCShem(request):
    parametrsGeneratedCircuit = getLevelParameter(request.level)
    myParam = myParametersForGeneratedCircuit(request.type, getLevelParameter(request.level))
    answer = myAnswer(getAnswerList(simulate_circuit(myParam)),
                      timeAnswer(parametrsGeneratedCircuit.TimePulse.Value))
    jsonAnswer = JsonAnswer(id               = request.id                     ,
                            parameterCircuit = parametrsGeneratedCircuit      ,
                            assignment       = questionForTheTask(answer.time , parametrsGeneratedCircuit.TimePulse.Value,parametrsGeneratedCircuit),
                            answer           = answer                         ,
                            level            = request.level                  ,
                            type             = request.type                    )

    print(jsonAnswer.model_dump_json())
    print(visual_result(myParam))


    return jsonAnswer




# json_date = Path("data.json").read_text()
# generatedRLCShem(json_date)