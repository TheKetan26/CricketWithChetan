from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads


from .functions import calculate, update, transform, clean, extract


@csrf_exempt
def analyse(request):
    if request.method == 'POST':
        body = loads(request.body.decode('utf-8'))
        response = calculate.performance(body['teams'], body['players'], body['type'], body['opposition'])

    return JsonResponse(response)


@csrf_exempt
def get_teams(request):
    if request.method == 'POST':
        body = loads(request.body.decode('utf-8'))
        try:
            response = extract.teams(body['type'])


    return JsonResponse({
        'teams': response
    })


@csrf_exempt
def get_players(request):
    if request.method == 'POST':
        body = loads(request.body.decode('utf-8'))
        response = extract.players(body['team'], body['type'])

    return JsonResponse(response)


@csrf_exempt
def get_player_state(request):
    if request.method == 'POST':
        body = loads(request.body.decode('utf-8'))
        response = extract.player_state(body['type'], body['team'], body['player'], body['role'])

    return JsonResponse(response)