from app.db.models import *


def get_sys_config(category: str, key: str, default=None):
    try:
        config = SysConfig.get((SysConfig.categroy == category) & (SysConfig.key == key) & (SysConfig.enabled == "1"))
        return config.value
    except SysConfig.DoesNotExist:
        return default


def set_sys_config(category: str, key: str, value: str, enabled: str = "1"):
    try:
        config = SysConfig.get((SysConfig.categroy == category) & (SysConfig.key == key))
        config.value = value
        config.enabled = enabled
        config.save()
    except SysConfig.DoesNotExist:
        pass
