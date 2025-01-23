import flet as ft
from app import Aplicacion


def main(page: ft.Page):
    app = Aplicacion(page)
    app.show_pokedex()
    
if __name__ == "__main__":
    ft.app(target=main)