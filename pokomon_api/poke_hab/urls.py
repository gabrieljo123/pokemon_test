from poke_hab.views import GetPokemonHabilities
from django.urls import path, re_path


app_name = "poke_hab"
urlpatterns = [
    re_path(r"^pokemon/(?P<pokemon_name>[0-9A-Za-z_\-]+)$", GetPokemonHabilities.as_view({'get': 'list'}), name="pokemon_view")
    ]