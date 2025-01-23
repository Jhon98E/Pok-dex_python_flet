import flet as ft
import requests
import time

URL_API = "https://pokeapi.co/api/v2/pokemon/"

class PokedexFunciones:
    def __init__(self, page):
        self.page = page
        self.pokemon_id = 0 # Pokémon inicial

    def peticion_api(self, url):
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            return respuesta.json()
        return None

    def actualizar_pokemon(self, texto, imagen):
        resultado = self.peticion_api(URL_API + str(self.pokemon_id))
        if not resultado:
            texto.value = "Error al obtener datos del Pokémon."
            texto.update()
            return

        # Actualiza la información del Pokémon
        informacion_pokemon = f'Nombre: {resultado["name"].capitalize()}\nHabilidades: '

        for elemento in resultado['abilities']:
            informacion_pokemon += f'{elemento["ability"]["name"]}\n'

        informacion_pokemon += f'Tipo: '
        for elemento in resultado['types']:
            informacion_pokemon += f'{elemento["type"]["name"]}\n'

        informacion_pokemon += f'Altura: {resultado["height"]} dm\n'
        texto.value = informacion_pokemon

        # Actualiza la imagen
        url_img = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{self.pokemon_id}.png'
        imagen.src = url_img

        texto.update()
        imagen.update()

    def incrementar_pokemon(self, texto, imagen):
        self.pokemon_id = (self.pokemon_id + 1) % 1025 or 1
        self.actualizar_pokemon(texto, imagen)

    def decrementar_pokemon(self, texto, imagen):
        self.pokemon_id = (self.pokemon_id - 1) % 1025 or 1025
        self.actualizar_pokemon(texto, imagen)

    def blinking(self, led_azul):
        while True:
            time.sleep(0.1)
            led_azul.bgcolor = ft.Colors.BLUE_300
            self.page.update()
            time.sleep(0.1)
            led_azul.bgcolor = ft.Colors.BLUE
            self.page.update()