import flet

from app.view.common.controls import ConfigRow


class BasicView:
    def __init__(self):
        self.layout = flet.Ref[flet.Container]()

    def build(self):
        self.layout.current = flet.Container(
            content=flet.Column(
                controls=[
                    ConfigRow("用户名", "1"),
                    ConfigRow("年龄", 12),
                    ConfigRow("价格", 3.14),
                    ConfigRow("是否开启", True),
                ]
            ),
            margin=10,
        )
        return self.layout.current
