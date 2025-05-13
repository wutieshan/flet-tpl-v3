from app.config.sys_default import sys_default_configs
from app.db.models import *
from app.utils.log_util import log


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


def init_sys_config():
    for config in sys_default_configs:
        if not SysConfig.select().where((SysConfig.categroy == config["categroy"]) & (SysConfig.key == config["key"])).exists():
            SysConfig.create(**config)
            log.info(f"create sys config: {config['categroy']}.{config['key']}")


def insert_db_default_data():
    init_sys_config()
