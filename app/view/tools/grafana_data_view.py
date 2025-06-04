import flet


class GrafanaDataView:
    def __init__(self):
        self.layout = flet.Ref[flet.Container]()

    def build(self):
        self.layout.current = flet.Container(content=flet.Text(""))
        return self.layout.current
