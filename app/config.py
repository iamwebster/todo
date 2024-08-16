import os 
from dotenv import load_dotenv


load_dotenv()


class MysqlConfig:
    def __init__(self, env: dict):
        self.host = env.get("MYSQL_HOST", "localhost")
        self.port = env.get("MYSQL_PORT", 3306)
        self.username = env.get("MYSQL_USERNAME", "root")
        self.password = env.get("MYSQL_PASSWORD", "root")
        self.database = env.get("MYSQL_DATABASE", "tasks_db")


mysql_config = MysqlConfig(os.environ)
