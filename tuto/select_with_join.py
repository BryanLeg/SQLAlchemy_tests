from main import session
from models import User, Comment
from sqlalchemy import select

statement = select(Comment).join(Comment.user).where(
    User.username == 'Bryan'
)

result = session.scalars(statement).all()

print(result)
