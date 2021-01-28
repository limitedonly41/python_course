import asyncio
import asyncpg
from datetime import date
async def main():
    conn = await asyncpg.connect(user='postgres', password='my00pass',
                                 database='demo', host='127.0.0.1')
    # values = await conn.execute(
    #     "INSERT INTO users(name, birth_date) VALUES($1, $2)",
    #     "Ann",
    #     date(1990, 3 ,15)
    # )
    rows = await conn.fetch("SELECT * FROM users;")
    for row in rows:
        print(row)

    john = await conn.fetchrow("SELECT * FROM users WHERE name = 'John';")
    print(john)
    await conn.close()

if __name__ == '__main__':
    asyncio.run(main())