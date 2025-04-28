import flet

from app.components.router import Router
from app.db.utils import get_sys_config, set_sys_config
from app.utils.log_util import log


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

        self._set_page_on_resized()

    def _init_page(self):
        self.page.title = "Flet tpl app v3"
        self.page.theme_mode = flet.ThemeMode.LIGHT
        self.page.window.width = float(get_sys_config("app.ui", "window_width"))
        self.page.window.height = float(get_sys_config("app.ui", "window_height"))

    def _init_routes(self):
        self.router.add_route("/", lambda: flet.Text("首页"))
        # tools
        self.router.add_route("/tools/apitest", lambda: flet.Text("Api测试工具"))
        self.router.add_route("/tools/process", lambda: flet.Text("进程管理"))
        self.router.add_route("/tools/service", lambda: flet.Text("服务管理"))
        self.router.add_route("/tools/logs", lambda: flet.Text("日志查看"))
        # users
        self.router.add_route("/users/list", lambda: flet.Text("用户列表"))
        self.router.add_route("/users/roles", lambda: flet.Text("角色管理"))
        self.router.add_route("/users/permissions", lambda: flet.Text("权限设置"))
        # settings
        self.router.add_route("/settings/basic", lambda: flet.Text("基本设置"))
        self.router.add_route("/settings/network", lambda: flet.Text("网络设置"))
        self.router.add_route("/settings/security", lambda: flet.Text("安全设置"))

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
        return flet.Container(
            content=flet.Column(
                controls=[
                    self._create_nav_item(
                        "首页",
                        flet.Icons.HOME,
                        "/",
                    ),
                    self._create_nav_item(
                        "工具",
                        flet.Icons.CONSTRUCTION,
                        "/tools",
                        [
                            self._create_submenu_item("Api测试", "/tools/apitest"),
                            self._create_submenu_item("进程管理", "/tools/process"),
                            self._create_submenu_item("服务管理", "/tools/service"),
                            self._create_submenu_item("日志查看", "/tools/logs"),
                        ],
                    ),
                    self._create_nav_item(
                        "用户管理",
                        flet.Icons.GROUP,
                        "/users",
                        [
                            self._create_submenu_item("用户列表", "/users/list"),
                            self._create_submenu_item("角色管理", "/users/roles"),
                            self._create_submenu_item("权限设置", "/users/permissions"),
                        ],
                    ),
                    self._create_nav_item(
                        "系统设置",
                        flet.Icons.SETTINGS,
                        "/settings",
                        [
                            self._create_submenu_item("基本设置", "/settings/basic"),
                            self._create_submenu_item("网络设置", "/settings/network"),
                            self._create_submenu_item("安全设置", "/settings/security"),
                        ],
                    ),
                ],
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
            content=self.router.navigate("/"),  # 默认显示首页
            expand=True,
            padding=10,
        )

    def _create_main_layout(self) -> flet.Row:
        self.main_layout = flet.Row(
            controls=[self.nav_bar, self.divider, self.content_area],
            expand=True,
            spacing=0,
        )
        self.page.add(self.main_layout)
        return self.main_layout

    def _set_page_on_resized(self):
        def on_resized(e):
            set_sys_config("app.ui", "window_width", str(e.width))
            set_sys_config("app.ui", "window_height", str(e.height))
            # log.info(f"adjust window size: {e.width}x{e.height}")

        self.page.on_resized = on_resized

    def _navigate(self, route: str):
        self.content_area.content = self.router.navigate(route)
        self.page.update()
