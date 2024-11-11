import flet as ft


class AdaptiveNavigationBarDestination(ft.NavigationBarDestination):
    def __init__(self, ios_icon, android_icon, label, page: ft.Page):
        super().__init__()
        self.page = page
        self._ios_icon = ios_icon
        self._android_icon = android_icon
        self.label = label

    def build(self):
        # Set icon based on platform
        self.icon = (
            self._ios_icon
            if self.page.platform in [ft.PagePlatform.IOS, ft.PagePlatform.MACOS]
            else self._android_icon
        )
        return self


class AppController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.body = None

    def setup_page(self):
        self.page.adaptive = True
        self.page.fonts = {
            "poppins": "fonts/Poppins.ttf"
        }
        self.page.window.width = 360
        self.page.window.height = 720
        self.page.padding = 0

    def setup_appbar(self):
        self.page.appbar = ft.AppBar(
            leading=ft.TextButton("New", style=ft.ButtonStyle(padding=0)),
            title=ft.Text("Tidyfy"),
            actions=[
                ft.IconButton(ft.cupertino_icons.ADD, style=ft.ButtonStyle(padding=0))
            ],
            bgcolor=ft.colors.with_opacity(0.04, ft.cupertino_colors.SYSTEM_BACKGROUND),
        )

    def create_body(self):
        self.body = ft.Container(
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["0xff1f005c", "0xffffb56b"]
            ),
            expand=True,
            border_radius=16,
        )

    def create_card(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

    def setup_navigation_bar(self):
        self.page.navigation_bar = ft.NavigationBar(
            selected_index=2,
            destinations=[
                AdaptiveNavigationBarDestination(
                    ios_icon=ft.cupertino_icons.PERSON_3_FILL,
                    android_icon=ft.icons.PERSON,
                    label="Contacts",
                    page=self.page
                ),
                AdaptiveNavigationBarDestination(
                    ios_icon=ft.cupertino_icons.CHAT_BUBBLE_2,
                    android_icon=ft.icons.CHAT,
                    label="Chats",
                    page=self.page
                ),
                ft.NavigationBarDestination(
                    icon=ft.cupertino_icons.SETTINGS,
                    label="Settings",
                ),
            ],
        )

    def build(self):
        self.setup_page()
        self.setup_appbar()
        self.create_body()
        self.page.add(self.body)
        self.page.add(self.create_card())
        self.setup_navigation_bar()
        self.page.update()
