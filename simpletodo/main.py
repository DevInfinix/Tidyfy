from components.controls import *

body = Container(
  Column([
    Banner("Salokhiddinov").build(),
    TaskList().build()
  ],spacing=0),
  expand=True,
  bgcolor=conf.blue
)

def main(page:Page):
  page.fonts = {
    "poppins":"fonts/Poppins.ttf"
  }
  page.window.width = 360
  page.window.height = 720
  page.window.bgcolor = conf.blue
  page.bgcolor = conf.blue
  page.padding = 0
  page.add(
    SafeArea(
      body,expand=True
    )
  )
  page.update()

app(main,assets_dir='assets')