from components.controls import AppController
import flet as ft
from flet import *

def main(page: ft.Page):
    app_controller = AppController(page)
    app_controller.build()


app(main, assets_dir='assets')
