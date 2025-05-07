import enum
from typing import TypeAlias

import flet

VT: TypeAlias = int | float | str | bool | list


class ConfigRow(flet.Row):
    def __init__(self, label: str, value: VT, *, _input: flet.Control = None, tooltip: str = None):
        super().__init__()

        self._label = label
        self._value = value
        self._input = _input
        self._tooltip = tooltip or ""

        # self._label_control = self._create_label_control()
        self._input_control = self._create_input_control()
        self.controls = [self._input_control]

    def _create_label_control(self) -> flet.Text:
        return flet.Text(
            value=self._label,
            width=80,
            height=24,
            text_align=flet.TextAlign.RIGHT,
            bgcolor=flet.colors.CYAN,
            weight=flet.FontWeight.BOLD,
        )

    def _create_input_control(self) -> flet.Control:
        # TODO: take self._input into account
        if isinstance(self._value, bool):
            return flet.Switch(value=self._value, label=self._label, label_position=flet.LabelPosition.RIGHT)
        else:
            return flet.TextField(value=self._tostr(), label=self._label)

    def _tostr(self) -> str:
        if isinstance(self._value, (int, float, str)):
            return f"{self._value}"
        elif isinstance(self._value, bool):
            return "true" if self._value else "false"
        elif isinstance(self._value, list):
            return ",".join(self._value)
        else:
            raise NotImplementedError(f"{self._value}: {type(self._value)}")

    def _on_change(self, e):
        pass

    def get(self) -> VT:
        pass

    def set(self, value: VT):
        pass
