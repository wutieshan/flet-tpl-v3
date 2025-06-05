import enum
import threading

import pynput

from app.utils.log_util import log


class AutoClick:
    """
    自动鼠标点击

    自定义设置
        1. 鼠标点击的频率
        2. 鼠标按键选择
        3.
    """

    class MouseButton(enum.Enum):
        LEFT = "left"
        RIGHT = "right"
        MIDDLE = "middle"
        X1 = "x1"
        X2 = "x2"

    def __init__(self):
        # options
        self._freq = 500  # 鼠标点击的频率(ms)
        self._button = AutoClick.MouseButton.LEFT  # 鼠标按键选择

        # controllers
        self._ctrl_mouse = pynput.mouse.Controller()
        self._ctrl_keyboard = pynput.keyboard.Controller()

    def __del__(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def finish(self):
        pass
