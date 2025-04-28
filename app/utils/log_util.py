import logging
import logging.config
import typing

from app.config.config import config
from app.utils.file_util import FileUtil


class LogUtil:
    Config: typing.TypeAlias = str | typing.Mapping
    LogLevel: typing.TypeAlias = int | str

    def __init__(self, name: str, config: Config):
        """
        params:
            - config: a dict or a str representing path of config file
        """
        self._stacklevel = 2
        self._logger = logging.getLogger(name)
        logging.config.dictConfig(self._load_config(config))

    def _load_config(self, config: Config) -> dict:
        if isinstance(config, str):
            return FileUtil.parse_dict(config)
        elif isinstance(config, typing.Mapping):
            return dict(config)
        else:
            # TODO: given a default config may be useful
            raise TypeError(f"config should be either str or mapping, got {type(config)}")

    def add_handler(self, handler: logging.Handler):
        self._logger.addHandler(handler)

    def set_level(self, level: LogLevel):
        self._logger.setLevel(level)

    def debug(self, msg: str, **kwargs) -> None:
        self._logger.debug(msg, stacklevel=self._stacklevel, **kwargs)

    def info(self, msg: str, **kwargs) -> None:
        self._logger.info(msg, stacklevel=self._stacklevel, **kwargs)

    def warning(self, msg: str, **kwargs) -> None:
        self._logger.warning(msg, stacklevel=self._stacklevel, **kwargs)

    def error(self, msg: str, **kwargs) -> None:
        self._logger.error(msg, stacklevel=self._stacklevel, exc_info=True, **kwargs)

    def critical(self, msg: str, **kwargs) -> None:
        self._logger.critical(msg, stacklevel=self._stacklevel, exc_info=True, **kwargs)


# singleton
log = LogUtil(name=config.get("app.logger"), config=config.get("app.log_filepath"))
