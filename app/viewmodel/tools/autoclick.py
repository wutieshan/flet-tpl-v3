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
        self._click_interval = 500  # 鼠标点击的间隔(ms)
        self._click_button = AutoClick.MouseButton.LEFT  # 鼠标按键选择
        self._start_pause_key = pynput.keyboard.Key.f1  # 状态切换按键: 开始, 暂停

        # controllers
        self._ctrl_mouse = pynput.mouse.Controller()
        # self._ctrl_keyboard = pynput.keyboard.Controller()

        # listeners
        # self._lsr_mouse = pynput.mouse.Listener()
        self._lsr_keyboard = pynput.keyboard.Listener(on_press=self.on_keyboard_press, on_release=self.on_keyboard_release)

        # global states
        self._is_running = True
        self._is_clicking = False

        #
        threading.Thread(target=self._do_click, daemon=True).start()

    def __del__(self):
        self._is_running = False

    def on_keyboard_press(self, key):
        pass

    def on_keyboard_release(self, key):
        if key == self._start_pause_key:
            self._is_clicking = not self._is_clicking

    def _do_click(self):
        while self._is_running:
            pass
