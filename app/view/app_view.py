import importlib

import flet

from app.components.router import Router
from app.config.routes import routes
from app.db.utils import get_sys_config, set_sys_config


class AppView:
    def __init__(self, page: flet.Page):
        self.page = page
        self.router = Router()

        self._init_page()
        self._init_routes()
        self.nav_bar = self._create_nav_bar()
        self.divider = self._create_divider()
        self.content_area = self._create_content_area()
        self.main_layout = self._create_main_layout()

        self._set_window_event()

    def _init_page(self):
        self.page.title = "Flet tpl app v3"
        self.page.theme_mode = flet.ThemeMode.LIGHT
        self.page.window.center()
        self.page.window.width = float(get_sys_config("app.ui", "window_width"))
        self.page.window.height = float(get_sys_config("app.ui", "window_height"))

    def _init_routes(self):
        """
        初始化路由, 规则如下:
            1. 每一条路由规则包含字段:
                - path
                - title: 菜单名称
                - icon: 菜单图标, 仅一级菜单
                - viewpath: 对应视图模块所在位置, 相对于app.view
                - view: 视图类名, 要求暴露build()方法用于构建ui
                - submenu: 子菜单路由
        """
        modprefix = "app.view"
        for route in routes:
            if route.get("submenus"):
                for submenu in route["submenus"]:
                    path = f"{route['path']}{submenu['path']}"
                    if submenu.get("viewpath"):
                        mod = importlib.import_module(f"{modprefix}.{submenu['viewpath']}")
                        self.router.add_route(path, lambda data=submenu["view"]: getattr(mod, data)().build())
                    else:
                        self.router.add_route(path, lambda data=path: flet.Text(data))
            else:
                path = route["path"]
                if route.get("viewpath"):
                    mod = importlib.import_module(f"{modprefix}.{route['viewpath']}")
                    self.router.add_route(path, lambda data=route["view"]: getattr(mod, data)().build())
                else:
                    self.router.add_route(path, lambda data=path: flet.Text(data))

    def _create_submenu_item(self, text: str, route: str):
        return flet.Container(
            content=flet.Row(
                controls=[
                    flet.Text(text, size=14),
                ],
                alignment=flet.MainAxisAlignment.START,
                spacing=10,
            ),
            padding=flet.padding.only(left=40, top=8, bottom=8),
            on_click=lambda _: self._navigate(route),
            border_radius=5,
            ink=True,
        )

    def _create_nav_item(self, text: str, icon: str, route: str, submenu_items=None):
        # menu items without submenu
        if submenu_items is None:
            return flet.Container(
                content=flet.Row(
                    controls=[
                        flet.Icon(icon),
                        flet.Text(text, expand=True),
                    ],
                    alignment=flet.MainAxisAlignment.START,
                    spacing=6,
                ),
                padding=10,
                on_click=lambda _: self._navigate(route),
                border_radius=5,
                ink=True,
            )

        is_expanded = flet.Ref[bool]()
        is_expanded.current = False

        def toggle_submenu(e):
            is_expanded.current = not is_expanded.current
            submenu.visible = is_expanded.current
            icon_control.name = flet.icons.KEYBOARD_ARROW_DOWN if is_expanded.current else flet.icons.KEYBOARD_ARROW_RIGHT
            self.nav_bar.update()

        icon_control = flet.Icon(flet.icons.KEYBOARD_ARROW_RIGHT)

        menu_item = flet.Container(
            content=flet.Row(
                controls=[
                    flet.Icon(icon),
                    flet.Text(text, expand=True),
                    icon_control,
                ],
                alignment=flet.MainAxisAlignment.START,
                spacing=6,
            ),
            padding=10,
            on_click=toggle_submenu,
            border_radius=5,
            ink=True,
        )

        submenu = flet.Column(
            controls=submenu_items or [],
            visible=False,
            spacing=0,
        )

        return flet.Column(
            controls=[menu_item, submenu],
            spacing=0,
        )

    def _create_nav_bar(self) -> flet.Container:
        menus = []
        for route in routes:
            submenu_items = None
            if route.get("submenus"):
                submenu_items = [self._create_submenu_item(submenu["title"], f"{route['path']}{submenu['path']}") for submenu in route["submenus"]]

            menus.append(self._create_nav_item(route["title"], route["icon"], route["path"], submenu_items))

        return flet.Container(
            content=flet.Column(
                controls=menus,
                spacing=5,
                scroll=flet.ScrollMode.AUTO,
            ),
            width=float(get_sys_config("app.ui", "nav_width")),
            padding=10,
            bgcolor=flet.Colors.BLUE_GREY_50,
            height=5000,  # TODO: a temp solution, set a very large height
        )

    def _create_divider(self) -> flet.GestureDetector:
        def on_hover(e):
            e.control.bgcolor = flet.Colors.BLUE if e.data == "true" else flet.Colors.GREY_300

        def update_nav_width(delta):
            new_width = max(160, min(320, self.nav_bar.width + delta))
            self.nav_bar.width = new_width
            set_sys_config("app.ui", "nav_width", str(new_width))
            self.page.update()

        return flet.GestureDetector(
            content=flet.Container(
                content=flet.VerticalDivider(),
                width=5,
                bgcolor=flet.Colors.GREY_300,
            ),
            on_hover=on_hover,
            mouse_cursor=flet.MouseCursor.RESIZE_COLUMN,
            drag_interval=10,
            on_pan_update=lambda e: update_nav_width(e.delta_x),
        )

    def _create_content_area(self) -> flet.Container:
        return flet.Container(
            content=self.router.navigate("/"),
            expand=True,
            padding=0,
        )

    def _create_main_layout(self) -> flet.Row:
        self.main_layout = flet.Row(
            controls=[self.nav_bar, self.divider, self.content_area],
            expand=True,
            spacing=0,
        )
        self.page.add(self.main_layout)
        return self.main_layout

    def _set_window_event(self):
        def on_event(e: flet.WindowEvent):
            if e.type == flet.WindowEventType.RESIZED:
                # log.info(f"window resized: {self.page.window.width}x{self.page.window.height}")
                set_sys_config("app.ui", "window_width", str(self.page.window.width))
                set_sys_config("app.ui", "window_height", str(self.page.window.height))

        self.page.window.on_event = on_event

    def _navigate(self, route: str):
        self.content_area.content = self.router.navigate(route)
        self.page.update()
