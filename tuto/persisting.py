from models import User, Comment
from main import session

user1 = User(
    username = "Bryan",
    email_adress = "ssgsfgs@dfsf.com",
    comments = [
        Comment(text = "Heloo"),
        Comment(text = "Hi")
    ]
)

paul = User(
    username = "Paul",
    email_adress = "paul@dfsf.com",
    comments = [
        Comment(text = "Hi, I'm Paul"),
        Comment(text = "Salute")
    ]
)

cathy = User(
    username = "Cathy",
    email_adress = "cathy@dfsf.com"
)

session.add_all([user1, paul, cathy])

session.commit()