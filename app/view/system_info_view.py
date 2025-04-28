import platform
import threading

import flet
import psutil


class SystemInfoView:
    def __init__(self):
        self._create_layout()
        self.activated = threading.Event()
        self.activated.set()

    def _create_layout(self):
        self.system_info = flet.Column(
            controls=[
                flet.Text("系统信息", size=20, weight=flet.FontWeight.BOLD),
                flet.Text(f"操作系统: {platform.system()} {platform.release()}"),
                flet.Text(f"Python版本: {platform.python_version()}"),
            ],
            spacing=10,
        )

        self.cpu_usage = flet.ProgressBar(width=300)
        self.cpu_text = flet.Text("CPU使用率: 0%")

        self.memory_usage = flet.ProgressBar(width=300)
        self.memory_text = flet.Text("内存使用率: 0%")

        self.disk_usage = flet.ProgressBar(width=300)
        self.disk_text = flet.Text("磁盘使用率: 0%")

        self.layout = flet.Column(
            controls=[
                self.system_info,
                flet.Divider(),
                flet.Text("资源使用情况", size=20, weight=flet.FontWeight.BOLD),
                self.cpu_text,
                self.cpu_usage,
                self.memory_text,
                self.memory_usage,
                self.disk_text,
                self.disk_usage,
            ],
            spacing=20,
            alignment=flet.MainAxisAlignment.START,
            horizontal_alignment=flet.CrossAxisAlignment.START,
            expand=True,
            scroll=flet.ScrollMode.AUTO,
        )

    def update_info(self):
        cpu_percent = psutil.cpu_percent()
        self.cpu_usage.value = cpu_percent / 100
        self.cpu_text.value = f"CPU使用率: {cpu_percent}%"

        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        self.memory_usage.value = memory_percent / 100
        self.memory_text.value = f"内存使用率: {memory_percent}% ({memory.used / (1024**3):.1f}GB / {memory.total / (1024**3):.1f}GB)"

        disk = psutil.disk_usage("/")
        disk_percent = disk.percent
        self.disk_usage.value = disk_percent / 100
        self.disk_text.value = f"磁盘使用率: {disk_percent}% ({disk.used / (1024**3):.1f}GB / {disk.total / (1024**3):.1f}GB)"

        return self.layout
