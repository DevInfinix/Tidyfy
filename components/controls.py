from flet import *
import components.conf as conf
from helpers import get_time_of_day

class Banner(object):
    def __init__(self, app_name):
        self.app_name = app_name
        self.text_field = Text(
            f"Good {get_time_of_day()} Infinix!",
            size=26, weight='w900',
            bottom=40, left=30,
            font_family='poppins',
            color=conf.white
        )
        self.icon_button = IconButton(
            icons.MENU,
            icon_color=conf.white, icon_size=30
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
                        bottom_left=0, bottom_right=0
                    )
                ),
                self.text_field,
                self.menu_button,
            ])
        )

    def build(self):
        return self.body

class InventoryList(object):
    def __init__(self):
        self.radius = 25
        self.item_list = []
        self.new_item = None
        self.load_items()
        self.add_button = Container(
            IconButton(
                icons.ADD,
                icon_color=conf.white,
                icon_size=30,
                on_click=self.add_new_item
            ),
            border_radius=360,
            bgcolor=conf.black,
            bottom=30, right=16,
            animate=Animation(600, AnimationCurve.BOUNCE_IN_OUT)
        )
        self.body = Container(
            Stack([
                Column(self.item_list),
                self.add_button
            ]),
            bgcolor=conf.white,
            expand=True,
            margin=margin.only(top=-self.radius),
            padding=padding.only(
                left=10, right=10, top=16, bottom=0
            ),
            border_radius=border_radius.only(
                top_left=self.radius,
                top_right=self.radius
            ), animate=Animation(600, AnimationCurve.BOUNCE_OUT)
        )

    def load_items(self):
        # Load some sample items to start with
        self.item_list = [
            ItemCard("Laptop", "Electronics", "1500", "2023-06-15").build(),
            ItemCard("Desk Lamp", "Furniture", "40", "2022-09-01").build(),
        ]

    def add_new_item(self, e):
        if self.add_button.content.icon == icons.ADD:
            self.new_item = NewItemForm(self)
            self.item_list.insert(0, self.new_item.build())
            self.add_button.content.icon = icons.CHECK
            self.body.update()
        else:
            new_item_data = self.new_item.get_item_data()
            if new_item_data:
                new_item = ItemCard(*new_item_data).build()
                self.item_list.insert(0, new_item)
            self.item_list.pop(0)
            self.add_button.content.icon = icons.ADD
            self.body.update()

    def build(self):
        return self.body

class ItemCard(object):
    def __init__(self, name, category, value, purchase_date):
        self.name = name
        self.category = category
        self.value = value
        self.purchase_date = purchase_date
        self.text_field = Text(
            f"{self.name} - {self.category} (${self.value})",
            color=conf.black,
            font_family='poppins',
            weight='w450',
            size=16
        )
        self.remove_button = Container(
            Icon(icons.DELETE, color=conf.white, scale=0.8),
            bgcolor=conf.red_pink,
            border_radius=8,
            padding=5,
            alignment=alignment.center_right
        )
        self.body = Dismissible(
            Container(
                Row([self.text_field]),
                animate=Animation(600),
            ),
            secondary_background=self.remove_button,
        )

    def build(self):
        return self.body

class NewItemForm(object):
    def __init__(self, control):
        self.control = control
        self.name_field = TextField(hint_text="Item Name", autofocus=True)
        self.category_field = TextField(hint_text="Category")
        self.value_field = TextField(hint_text="Value ($)", keyboard_type=KeyboardType.NUMBER)
        self.date_field = TextField(hint_text="Purchase Date (YYYY-MM-DD)")
        self.body = Container(
            Row([
                self.name_field,
                self.category_field,
                self.value_field,
                self.date_field
            ], alignment=MainAxisAlignment.CENTER),
            animate=Animation(600)
        )

    def get_item_data(self):
        return (
            self.name_field.value,
            self.category_field.value,
            self.value_field.value,
            self.date_field.value
        )

    def build(self):
        return self.body
