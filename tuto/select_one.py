from main import session
from models import User

Bryan = session.query(User).filter_by(username = "Bryan").first()

print(Bryan)