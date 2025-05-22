from DaoBase.BaseDao import BaseDAO
from Models.models import Person, Profile,Post


class UserDAO(BaseDAO):
    model = Person


class ProfileDAO(BaseDAO):
    model = Profile

class PostDAO(BaseDAO):
    model = Post

