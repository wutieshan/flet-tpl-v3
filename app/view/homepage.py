import flet


class HomepageView:
    def __init__(self):
        self.layout = flet.Ref[flet.Container]()
        self.greetings = "welcome, flet-tpl-v3!"

    def build(self):
        self.layout.current = flet.Container(
            content=flet.Stack(
                [
                    flet.Text(
                        spans=[
                            flet.TextSpan(
                                self.greetings,
                                flet.TextStyle(
                                    size=40,
                                    weight=flet.FontWeight.BOLD,
                                    foreground=flet.Paint(
                                        color=flet.colors.BLUE_700,
                                        stroke_width=6,
                                        style=flet.PaintingStyle.STROKE,
                                    ),
                                ),
                            ),
                        ],
                    ),
                    flet.Text(
                        spans=[
                            flet.TextSpan(
                                self.greetings,
                                flet.TextStyle(
                                    size=40,
                                    weight=flet.FontWeight.BOLD,
                                    color=flet.colors.GREY_300,
                                ),
                            ),
                        ],
                    ),
                ]
            ),
            alignment=flet.alignment.center,
        )
        return self.layout.current
