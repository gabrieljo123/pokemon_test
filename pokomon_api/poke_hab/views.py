from django.http import response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
import ipdb

import requests
# Create your views here.

class GetPokemonHabilities(viewsets.ModelViewSet):

    def list(self, request, pokemon_name, *args, **kwargs):
        r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}', auth=('user', 'pass'))
        data = r.json()
        abilities = data['abilities']
        new_dict = {}
        for ability in abilities:
            new_dict[ability['ability']['name']] = ability
        new_dict = sorted(new_dict.items())
        response = []
        for ability in new_dict:
            response.append(ability[1])
        return Response(response)