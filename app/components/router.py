import flet


class Router:
    def __init__(self):
        self.routes = {}
        self.current_route = None

    def add_route(self, path: str, view_func):
        self.routes[path] = view_func

    def navigate(self, path: str):
        if path in self.routes:
            self.current_route = path
            return self.routes[path]()
        return flet.Text(f"未找到路由: {path}")

    def get_current_route(self) -> str:
        return self.current_route
