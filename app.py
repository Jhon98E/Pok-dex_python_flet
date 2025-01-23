import flet as ft
import math
from componentes import Componente
from funciones import PokedexFunciones

class Aplicacion:
    def __init__(self, page:ft.Page):
        self.page = page
        self.page.title = "Pokédex"
        self.page.bgcolor = ft.Colors.RED_ACCENT_700
        self.page.window.width = 650
        self.page.window.height = 1000
        self.page.window.resizable = False
        self.page.window.maximizable = False
        self.Componente = Componente()
        self.funciones = PokedexFunciones(page)

    def show_pokedex(self):

        # Crear Componentes superiores(leds)
        led_azul = self.Componente.crear_led(
            color=ft.Colors.BLUE,
            size=70,
            border_color=ft.Colors.WHITE,
            border_width=5
        )
        led_rojo = self.Componente.crear_led(
            color=ft.Colors.RED_200,
            size=20,
        )
        led_amarillo = self.Componente.crear_led(
            color=ft.Colors.YELLOW,
            size=20,
        )
        led_verde = self.Componente.crear_led(
            color=ft.Colors.GREEN,
            size=20,
        )

        componentes_superiores = ft.Container(
            content=ft.Row(
                [
                    led_azul,
                    led_rojo,
                    led_amarillo,
                    led_verde,
                ],
                spacing=20,
            ),
            margin=ft.margin.all(10),
        )

        # Crear Componentes del medio(Pantalla)
        url_img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png"
        imagen = ft.Image(
            src=url_img,
            scale=10,
            width=30,
            height=30,
        )

        marco_pantalla = ft.Container(
            width=700,
            height=400,
            bgcolor=ft.Colors.WHITE,
            border_radius=ft.border_radius.only(10, 10, 100, 10),
            margin=ft.margin.only(left=15, top=30, right=15, bottom=30),
            alignment=ft.alignment.center,
        )

        pantalla_interior = ft.Container(
            width=500,
            height=315,
            bgcolor=ft.Colors.BLUE_200,
            border_radius=ft.border_radius.all(10),
            alignment=ft.alignment.center,
        )

        pantalla_interior.content = imagen
        marco_pantalla.content = pantalla_interior

        componentes_centrales = ft.Container(
            marco_pantalla
        )

        # Crear Componentes inferiores(Botones y panatalla de información)

        texto = ft.Text(
            value="...",
            size=20,
            color=ft.Colors.BLACK,
        )

        pantalla_informacion = ft.Container(
            content=ft.Column(
                [
                    texto,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=10,
            width=400,
            height=300,
            margin=ft.margin.only(left=15, top=30, right=15, bottom=30),
            bgcolor=ft.Colors.GREEN,
            border_radius=ft.border_radius.all(10),
        )

        triangulo_flechas = ft.Container(
            width=0,
            height=0,
            border=ft.border.Border(
                left=ft.border.BorderSide(40, "transparent"),   # Lado izquierdo
                right=ft.border.BorderSide(40, "transparent"),  # Lado derecho
                bottom=ft.border.BorderSide(50, "black")         # Lado inferior (color del triángulo)
            )
        )

        boton_up = ft.Container(
            triangulo_flechas,
            width=80,
            height=50,
            on_click=lambda e: self.funciones.incrementar_pokemon(texto, imagen),
        )

        boton_down = ft.Container(
            triangulo_flechas,
            rotate=ft.Rotate(angle=math.pi),
            width=80,
            height=50,
            on_click=lambda e: self.funciones.decrementar_pokemon(texto, imagen),
        )
        
        botones = ft.Column(
            [
                boton_up,
                boton_down,
            ],
            spacing=20,
        )

        componentes_inferiores = ft.Container(
            content=ft.Row(
                [
                    pantalla_informacion,
                    botones
                ],
                spacing=50,
            )
        )
            

        # Agregar componentes a la ventana
        self.page.add(
            componentes_superiores,
            componentes_centrales,
            componentes_inferiores
        )
        self.funciones.blinking(led_azul)