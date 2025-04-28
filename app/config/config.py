import dynaconf


class Config:
    def __init__(self):
        self.settings = dynaconf.Dynaconf(
            settings_files=["conf/global.toml", "conf/.local.toml"],
            envvar_prefix="FLET_TPL",
            environments=True,
            load_dotenv=True,
        )
        self._validate_config()

    def _validate_config(self) -> None:
        """验证必要的配置项是否存在"""
        required_settings = [
            "app.debug",
            "app.secret_key",
        ]
        
        for setting in required_settings:
            if not self.settings.get(setting):
                raise ValueError(f"missing required configuration: {setting}")

    def get(self, key: str, default=None):
        """获取配置项"""
        return self.settings.get(key, default)

    def is_debug(self) -> bool:
        """检查是否处于调试模式"""
        return self.get("app.debug")

config = Config()
