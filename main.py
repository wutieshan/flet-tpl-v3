import flet

from app.db.manager import dbm
from app.view.app_view import AppView


def main(page: flet.Page):
    dbm.init_db()

    AppView(page)


if __name__ == "__main__":
    flet.app(target=main, view=flet.AppView.FLET_APP_HIDDEN)
