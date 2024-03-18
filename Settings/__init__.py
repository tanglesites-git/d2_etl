from enum import Enum
from json import load
from pathlib import Path


class Dirs:
    ROOT = Path(__file__).parent.parent
    JSON = ROOT / "json"
    DATA = ROOT / "data"
    ASSETS = ROOT / "assets"
    ICONS = ASSETS / "icons"
    SCREENSHOTS = ASSETS / "screenshots"
    WATERMARKS = ASSETS / "watermarks"

    def create(self):
        self.JSON.mkdir(parents=True, exist_ok=True)
        self.DATA.mkdir(parents=True, exist_ok=True)
        self.ASSETS.mkdir(parents=True, exist_ok=True)
        self.ICONS.mkdir(parents=True, exist_ok=True)
        self.SCREENSHOTS.mkdir(parents=True, exist_ok=True)
        self.WATERMARKS.mkdir(parents=True, exist_ok=True)


class Files:
    ROOT = Path(__file__).parent.parent
    CONF = ROOT / "conf.json"
    MANIFEST = Dirs.DATA / "manifest.json"
    MANIFEST_DATA = Dirs.DATA / "manifest_data.db"
    WORLD_CONTENT = Dirs.DATA / "world_content.db"
    MSSQL_DB = Dirs.DATA / "d2db_mssql.db"
    MYSQL_DB = Dirs.DATA / "d2db_mysql.db"
    SQLITE_DB = Dirs.DATA / "d2db_sqlite.db"
    PGSQL_DB = Dirs.DATA / "d2db_pgsql.db"

    def create(self):
        self.CONF.touch(exist_ok=True)
        self.MANIFEST_DATA.touch(exist_ok=True)
        self.WORLD_CONTENT.touch(exist_ok=True)
        self.MSSQL_DB.touch(exist_ok=True)
        self.MYSQL_DB.touch(exist_ok=True)
        self.SQLITE_DB.touch(exist_ok=True)
        self.PGSQL_DB.touch(exist_ok=True)


with open(Files.CONF, "r", encoding="utf-8") as file:
    data = load(file)


class Environment(Enum):
    DEVELOPMENT = 1
    PRODUCTION = 2


class Settings:

    def __init__(self, api_key: str, base_address: str, env: str):
        self.ApiKey = api_key
        self.BaseAddress = base_address
        self.Environment = env


settings = Settings(data["ApiKey"], data["BaseAddress"], data["Environment"])
