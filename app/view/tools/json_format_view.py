import json

import flet


class JsonFormatView:
    def __init__(self):
        self.layout = flet.Ref[flet.Container]()
        self.input_field = flet.TextField(
            label="输入JSON",
            multiline=True,
            min_lines=10,
            max_lines=10,
            expand=True,
            border_color=flet.colors.BLUE_GREY_300,
        )
        self.output_field = flet.TextField(
            label="格式化后的JSON",
            multiline=True,
            min_lines=10,
            max_lines=10,
            expand=True,
            read_only=True,
            border_color=flet.colors.BLUE_GREY_300,
        )
        self.error_text = flet.Text(
            value="",
            color=flet.colors.RED,
            size=14,
        )

    def format_json(self, e, compress=False):
        try:
            js = json.loads(self.input_field.value)
            if compress:
                js_fmt = json.dumps(js, separators=(",", ":"))
            else:
                js_fmt = json.dumps(js, indent=4, ensure_ascii=False)
            self.output_field.value = js_fmt
            self.error_text.value = ""
        except json.JSONDecodeError as e1:
            self.error_text.value = f"JSON格式错误: {e1}"
            self.output_field.value = ""
        except Exception as e2:
            self.error_text.value = f"发生错误: {e2}"
            self.output_field.value = ""
        finally:
            self.layout.current.update()

    def clear_fields(self, e):
        self.input_field.value = ""
        self.output_field.value = ""
        self.error_text.value = ""
        self.layout.current.update()

    def build(self):
        self.layout.current = flet.Container(
            content=flet.Column(
                controls=[
                    flet.Row(
                        controls=[
                            flet.ElevatedButton(
                                "格式化",
                                on_click=lambda e: self.format_json(e, compress=False),
                                icon=flet.icons.FORMAT_INDENT_INCREASE,
                            ),
                            flet.ElevatedButton(
                                "压缩",
                                on_click=lambda e: self.format_json(e, compress=True),
                                icon=flet.icons.COMPRESS,
                            ),
                            flet.ElevatedButton(
                                "清空",
                                on_click=self.clear_fields,
                                icon=flet.icons.CLEAR_ALL,
                            ),
                        ],
                        alignment=flet.MainAxisAlignment.START,
                        spacing=10,
                    ),
                    flet.Column(
                        controls=[
                            self.input_field,
                            self.output_field,
                            self.error_text,
                        ],
                        expand=True,
                        spacing=20,
                    ),
                ],
                expand=True,
                spacing=20,
                scroll=flet.ScrollMode.AUTO,
                alignment=flet.MainAxisAlignment.START,
            ),
            padding=flet.padding.all(20),
            expand=True,
            height=5000,
        )
        return self.layout.current
