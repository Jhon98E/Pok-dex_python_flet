import flet as ft

class Componente:
    def crear_led(self, color:str, size:int, border_color:str = None, border_width:int = 0):
        return ft.Container(
            width=size,
            height=size,
            bgcolor=color,
            border=ft.border.all(color=border_color, width=border_width) if border_color else None,
            border_radius=ft.border_radius.all(50),
        )