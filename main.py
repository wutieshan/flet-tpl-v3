import flet

from app.db.manager import dbm
from app.db.utils import init_sys_config
from app.view.app_view import AppView


def main(page: flet.Page):
    AppView(page)


if __name__ == "__main__":
    dbm.init_db()
    init_sys_config()
    flet.app(target=main)
