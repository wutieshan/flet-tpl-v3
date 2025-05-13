import flet

from app.db.manager import dbm
from app.view.app_view import AppView


def main(page: flet.Page):
    AppView(page)


if __name__ == "__main__":
    dbm.init_db()
    flet.app(target=main, view=flet.AppView.FLET_APP_HIDDEN)
