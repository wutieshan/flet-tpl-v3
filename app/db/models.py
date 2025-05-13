import datetime
import importlib
import inspect

import peewee as pw

from app.utils.log_util import log

# a placeholder, will be initialized later
db_proxy = pw.DatabaseProxy()
now = datetime.datetime.now


def make_table_name(model_cls):
    """
    the rule for table name generates

    examples:
    User           -> t_user
    SysConfig      -> t_sys_config
    APIResponse    -> t_api_response
    WebHTTPRequest -> t_web_http_request
    OpenAI         -> t_open_ai
    """
    chars = list(model_cls.__name__)
    target = []
    for idx, ch in enumerate(chars):
        tmp = ""
        if idx > 0 and idx < len(chars) - 1 and ch.isupper() and (chars[idx - 1].islower() or chars[idx + 1].islower()):
            tmp += "_"
        tmp += ch.lower()
        target.append(tmp)
    return "t_" + "".join(target)


class BaseModel(pw.Model):
    class Meta:
        database = db_proxy
        legacy_table_names = False
        table_function = make_table_name

    def save(self, *args, **kwargs):
        if hasattr(self, "updated_at"):
            self.updated_at = now()
        return super().save(*args, **kwargs)

    @classmethod
    def update(cls, data=None, /, **update):
        if data is None:
            data = {}
        data["updated_at"] = now()
        return super().update(data, **update)

    @classmethod
    def init_default_data(cls):
        modprefix = "app.db.defaults"
        try:
            mod = importlib.import_module(f"{modprefix}.{cls._meta.table_name}")
            return getattr(mod, "data")
        except Exception:
            return []


class SysUser(BaseModel):
    """ "系统用户基本信息表"""

    userid = pw.CharField(unique=True)
    username = pw.CharField()
    password = pw.CharField(null=True)
    mobile = pw.CharField(null=True)
    mail = pw.CharField(null=True)
    status = pw.FixedCharField(max_length=1, default="0", help_text="用户状态: 0-正常,1-冻结,2-注销")
    created_at = pw.DateTimeField(default=now)
    updated_at = pw.DateTimeField(default=now)
    expires_at = pw.DateTimeField(default=lambda: now() + datetime.timedelta(days=30), help_text="账号密码过期时间")  # TODO: config


class SysConfig(BaseModel):
    """系统配置信息表"""

    categroy = pw.CharField()
    key = pw.CharField()
    value = pw.CharField()
    description = pw.TextField(null=True)
    enabled = pw.FixedCharField(max_length=1, default=1, help_text="是否启用配置: 0-禁用,1-启用")
    created_at = pw.DateTimeField(default=now)
    updated_at = pw.DateTimeField(default=now)

    @classmethod
    def init_default_data(cls):
        for config in super().init_default_data():
            if not cls.select().where((cls.categroy == config["categroy"]) & (cls.key == config["key"])).exists():
                cls.create(**config)
                log.info(f"create row for {cls.__name__}: {config['categroy']}.{config['key']}")


tables = [cls for cls in inspect.currentframe().f_globals.values() if inspect.isclass(cls) and cls is not BaseModel]
