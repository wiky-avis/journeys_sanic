import aiopg
from psycopg2.extras import DictCursor
from sqlalchemy.ext.asyncio import create_async_engine

DB_URL = 'postgresql://sanic:sanic@127.0.0.1:5432/test'


async def get_all_tours():
    query = 'SELECT id, title, description, departure FROM tour ;'
    async with aiopg.connect(DB_URL) as conn:
        async with conn.cursor(cursor_factory=DictCursor) as cur:
            await cur.execute(query)
            data = await cur.fetchall()
            return [dict(u) for u in data]
