from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

engine = create_engine("sqlite:///example.db")
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

posts_tags_table = Table(
    "posts_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),

)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_stuff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow())

    posts = relationship("Post", back_populates="author")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    author_id = Column(Integer, ForeignKey(User.id), nullable=False)

    author = relationship(User, back_populates="posts")
    tags = relationship("Tag", secondary=posts_tags_table, back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.title!r}, username={self.author!r})"

    def __repr__(self):
        return str(self)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    posts = relationship("Post", secondary=posts_tags_table, back_populates="tags")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"


def create_user(username: str) -> User:
    """
    :param username:
    :return:
    """

    u = User(username=username)
    session.add(u)
    session.commit()
    return u

def create_tags():
    tags = [Tag(name=name) for name in ("news", "flask", "django", "python")]
    post = Post(title="Flask vs Django", author_id=2)
    print(post)
    post.tags.extend(tags)

    session.commit()

    print(post, post.tags)
    for tag in tags:
        print(tag, tag.posts)

if __name__ == '__main__':
    Base.metadata.create_all()
    session = Session()

    posts_query = session.query(User).join(Post, User.id == Post.author_id).filter(Post.tags.any(Tag.name != "django"))
    print(posts_query)

    # create_user("Nick")
    # create_user("Sam")


    session.close()
