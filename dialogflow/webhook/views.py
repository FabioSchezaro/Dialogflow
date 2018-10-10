from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def index(request):
    return HttpResponse('Hello world')

@csrf_exempt
#require_POST
def dialogflow(request):
    req = json.loads(request.body)
    print('Request: ')
    print(json.dumps(req, indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    print (res)
    return HttpResponse(res, content_type='application/json')

def makeWebhookResult(req):
    if req.get('queryResult').get('action') != 'Dosagem':
        return {}
    result = req.get('queryResult')
    parameters = result.get('parameters')
    msg = result.get('fulfillmentMessages')
    if msg:
        verificaErro = "\n".join(map(lambda erros: ' '.join(erros.get('text').get('text')), msg))
    nameMed = parameters.get('NomeMedicamento')
    nameDosagem = parameters.get('DosagemMedicamento')
    tipoDosagem = parameters.get('TipoDosagemMedicamento')
    if msg and verificaErro != "":
        speech = verificaErro
    else:
        speech = 'Aplicado ' + str(nameDosagem) + str(tipoDosagem) + ' de ' + str(nameMed.title())

    print ('Response: ')
    print(speech)
    return {
        'fulfillmentText' : speech,
        'source' : 'Dr.Farmer'
    }