import flet


class AutoclickView:
    def __init__(self):
        self.layout = flet.Ref[flet.Container]()

    def build(self):
        self.layout.current = flet.Container()
        return self.layout.current
