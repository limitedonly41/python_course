import asyncio
from datetime import date

from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.Date(), nullable=False)

    def __str__(self):
        values = [f"{n}={getattr(self, n)}" for n in ("id", "name", "birth_date")]
        return f"{self.__class__.__name__}({','.join(values)})"
    __repr__ = __str__

async def main():
    await db.set_bind('postgresql://postgres:my00pass@localhost/demo')
    users = await db.all(User.query)
    print(users)
    ann = await User.get(2)
    print(ann)
    # sam = await User.create(name='Sam', birth_date=date(1998, 3, 17))
    # print(sam)
    john = await User.query.where(User.name=='John').gino.all()
    print(john)
if __name__ == '__main__':
    asyncio.run(main())
