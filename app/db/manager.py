from typing import Optional

import peewee as pw
from playhouse.db_url import connect

from app.config.config import config
from app.db.models import db_proxy, tables
from app.utils.log_util import log


class DBManager:
    def __init__(self):
        self.db: Optional[pw.Database] = None

    def init_db(self) -> None:
        try:
            db_url = config.get("app.db_url")
            if not db_url:
                raise ValueError("app.db_url is not configured")

            self.db = connect(db_url)
            db_proxy.initialize(self.db)

            self.create_tables()
            self.init_default_data()
            log.info("database initialized successfully")
        except Exception as e:
            log.error(f"failed to initialize database: {e}")
            raise

    def create_tables(self) -> None:
        try:
            with self.db:
                self.db.create_tables(tables)
            log.info("database tables created successfully")
        except Exception as e:
            log.error(f"failed to create tables: {e}")
            raise

    def init_default_data(self):
        for table in tables:
            table.init_default_data()

    def close(self) -> None:
        if self.db:
            self.db.close()
            log.info("database connection closed")

    def get_db(self) -> pw.Database:
        if not self.db:
            raise RuntimeError("database not initialized")
        return self.db


dbm = DBManager()
