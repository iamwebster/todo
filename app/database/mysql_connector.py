import asyncio 
import aiomysql 

from app.config import mysql_config


class MysqlConnector:
    def __init__(self, sql_query_create_table):
        self.sql_query_create_table = sql_query_create_table

    async def connect(self):
        loop = asyncio.get_event_loop()
        conn = await aiomysql.connect(
            host=mysql_config.host, port=int(mysql_config.port),
            user=mysql_config.username, password=mysql_config.password,
            db=mysql_config.database, loop=loop
        )

        async with conn.cursor() as cur:
            await cur.execute(self.sql_query_create_table)
            await conn.commit()

        return conn
    

class MysqlTodo(MysqlConnector):
    async def get_all_tasks(self):
        conn = await self.connect()

        async with conn.cursor(aiomysql.DictCursor) as cur:
            sql = "SELECT * FROM tasks"
            await cur.execute(sql)
            result = await cur.fetchall()

        conn.close()
        return result 

    async def create_new_task(self, task_data):
        conn = await self.connect()

        async with conn.cursor() as cur:
            sql = "INSERT INTO tasks (title, text) VALUES (%s, %s)"
            await cur.execute(sql, (task_data.title, task_data.text))
            await conn.commit()
        
        conn.close()
        return {"detail": "the task was successfully added"}
    
    async def get_detail_task(self, task_id):
        conn = await self.connect()

        async with conn.cursor(aiomysql.DictCursor) as cur:
            sql = "SELECT * FROM tasks WHERE id = %s"
            await cur.execute(sql, (task_id,))
            result = await cur.fetchone()

        conn.close()
        return result   
    
    async def update_task(self, task_id, task_data):
        conn = await self.connect()

        async with conn.cursor() as cur:
            sql = "UPDATE tasks SET title = %s, text = %s WHERE id = %s"
            await cur.execute(sql, (task_data.title, task_data.text, task_id))
            await conn.commit()
        
        conn.close()
        return {"detail": "the task was successfully updated"}
    
    async def delete_task(self, task_id):
        conn = await self.connect()

        async with conn.cursor() as cur:
            sql = "DELETE FROM tasks WHERE id = %s"
            await cur.execute(sql, (task_id))
            await conn.commit()
        
        conn.close()
        return {"detail": "the task was successfully deleted"}

    

connector = MysqlTodo(
    """CREATE TABLE IF NOT EXISTS tasks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    title VARCHAR(255) NOT NULL,
    text TEXT
    )"""
)