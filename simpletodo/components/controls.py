from flet import *
import components.conf as conf


class Banner(object):
  def __init__(self,username):
    self.username = username
    self.radius = 0
    self.text_field = Text(
      f"What's up {self.username}",
      size=26,weight='w900',
      bottom=40,left=30,
      font_family='poppins',
      color=conf.white
    )
    self.icon_button = IconButton(
      icons.MENU,
      icon_color=conf.white,icon_size=30
    )
    self.menu_button = Container(
      self.icon_button,
      padding=8
    )
    self.body = Container(
      Stack([
        Image(
          src="https://i.imghippo.com/files/N7I8U1719581813.png",
          border_radius=border_radius.only(
            bottom_left=self.radius,bottom_right=self.radius
            )
        ),
        self.text_field,
        self.menu_button,
      ])
    )
  def build(self):
    return self.body

class TaskList(object):
  def __init__(self):
    # super().__init__()
    self.radius = 25
    self.task_list = []
    self.new_task = None
    self.load_tasks()
    self.add_button = Container(
      IconButton(
        icons.ADD,
        icon_color=conf.white,
        icon_size=30,
        on_click=self.add_new_task
      ),
      border_radius=360,
      bgcolor=conf.light_blue,
      bottom=30,right=16,
      animate=Animation(600,AnimationCurve.BOUNCE_IN_OUT)
    )
    self.body = Container(
      Stack([
        Column(self.task_list),
        self.add_button
      ]),
      bgcolor=conf.white,
      expand=True,
      margin=margin.only(top=-self.radius),
      padding=padding.only(
        left=10,right=10,top=16,bottom=0
      ),
      border_radius=border_radius.only(
        top_left=self.radius,
        top_right=self.radius
      ),animate=Animation(600,AnimationCurve.BOUNCE_OUT)
    )

  def load_tasks(self):
      self.task_list = [
        Task(False,self,"Buy movie ticket for Friday").build(),
        Task(False,self,"Make Video about Flet").build(),  
      ]

  def add_new_task(self,e):
    if self.add_button.content.icon == icons.ADD:
      self.new_task = NewTask(self)
      self.task_list.insert(0,self.new_task.build())
      self.add_button.content.icon=icons.CHECK
      self.body.update()
    else:
      print(self.task_list)
      new_task = Task(False,self,self.new_task.get_value())
      self.task_list.remove(self.task_list[0])
      self.task_list.insert(0,new_task.build())
      self.add_button.content.icon=icons.ADD
      self.body.update()
      
  
  def build(self):
    return self.body

class Task(object):
  def __init__(self,value,control,text):
    self.value = value
    self.control = control
    self.text = text
    self.text_style = TextStyle(
      decoration_thickness=2,
    )
    self.text_field = Text(
      self.text,
      color=conf.black,
      font_family='poppins',
      weight='w450',
      size=16,
      style=self.text_style
    )
    self.remove_swipe = Container(
      Icon(
        icons.DELETE,
        color=conf.white,
        scale=0.8
      ),
      bgcolor=conf.red_pink,
      border_radius=8,
      padding=5,
      alignment=alignment.center_right
    )
    self.body = Dismissible(
      Container(
        Row([
          Checkbox(
            value=self.value,
            check_color=conf.white,
            active_color=conf.light_blue,
            overlay_color='transparent',
            on_change=self.on_change
          ),
          self.text_field
        ]),animate=Animation(600),
      ),on_dismiss=self.delete_task,
      secondary_background=self.remove_swipe
    )
  def delete_task(self):
    print(self.control.task_list)

  def on_change(self,e):
    if self.value == False:
      self.text_style.decoration = TextDecoration.LINE_THROUGH
      self.text_style.decoration_color = conf.gray
      self.text_field.color = conf.gray
      self.value = True
    else:
      self.text_style.decoration = TextDecoration.NONE
      self.text_style.decoration_color = conf.black
      self.text_field.color = conf.black
      self.value = False
    self.body.update()

  def build(self):
    return self.body

class NewTask(object):
  def __init__(self,control):
    self.control = control
    self.text_style = TextStyle(
      font_family='poppins',
      weight='w450'
    )
    self.text_field = TextField(
      color=conf.black,
      # font_family='poppins',
      # weight='w600',
      border=InputBorder.UNDERLINE,height=40,
      text_align='center',
      text_size=16,
      text_style=self.text_style,
      hint_text="New task name",
      autofocus=True,
      hint_style=TextStyle(color=conf.gray,size=16,font_family='poppins',weight='w450')
    )
    self.body = Container(
      Row([
        # Checkbox(
        #   value=False,
        #   check_color=conf.white,
        #   active_color=conf.light_blue,
        #   overlay_color='transparent',
        # ),
        self.text_field
      ],alignment=MainAxisAlignment.CENTER),animate=Animation(600)
    )
  def get_value(self):
    return self.text_field.value
  def build(self):
    return self.body